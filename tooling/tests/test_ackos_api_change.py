import base64
import contextlib
import io
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import ackos_api_change


class FakeAPIHandler(BaseHTTPRequestHandler):
    requests = []
    change_response = {"execution_id": "exec-test", "verified": True, "committed": True, "state": "committed"}

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        payload = json.loads(body.decode("utf-8"))
        type(self).requests.append((self.path, self.headers.get("Authorization"), payload))
        if self.path == "/v1/observations":
            response = {"observation_token": "opaque-test-token"}
        elif self.path == "/v1/changes":
            response = type(self).change_response
        else:
            self.send_error(404)
            return
        encoded = json.dumps(response).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, *_args):
        pass


class AckosAPIChangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), FakeAPIHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def setUp(self):
        FakeAPIHandler.requests = []
        FakeAPIHandler.change_response = {
            "execution_id": "exec-test",
            "verified": True,
            "committed": True,
            "state": "committed",
        }

    def run_client(self, content_file):
        env = {
            "ACKOS_API_BASE_URL": self.base_url,
            "ACKOS_API_BEARER_TOKEN": "test-secret",
            "ACKOS_API_REPOSITORY_ID": "disposable",
        }
        output = io.StringIO()
        errors = io.StringIO()
        with patch.dict(os.environ, env, clear=False), contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            code = ackos_api_change.main([
                "--branch", "test-branch",
                "--path", "README.md",
                "--content-file", str(content_file),
            ])
        return code, output.getvalue(), errors.getvalue()

    def test_observes_then_changes_with_returned_token(self):
        with tempfile.TemporaryDirectory() as directory:
            content_file = Path(directory) / "desired.bin"
            desired = b"updated bytes\x00\xff"
            content_file.write_bytes(desired)
            code, output, errors = self.run_client(content_file)

        self.assertEqual(code, 0, errors)
        self.assertEqual([item[0] for item in FakeAPIHandler.requests], ["/v1/observations", "/v1/changes"])
        observe, change = FakeAPIHandler.requests
        self.assertEqual(observe[1], "Bearer test-secret")
        self.assertEqual(observe[2], {"repository_id": "disposable", "branch": "test-branch", "path": "README.md"})
        self.assertEqual(change[1], "Bearer test-secret")
        self.assertEqual(change[2]["observation_token"], "opaque-test-token")
        self.assertEqual(change[2]["mode"], "100644")
        self.assertEqual(base64.b64decode(change[2]["content_base64"]), desired)
        self.assertNotIn("opaque-test-token", output + errors)
        self.assertNotIn("test-secret", output + errors)
        self.assertIn("verified and committed", output)

    def test_does_not_report_success_without_verification_and_commit(self):
        FakeAPIHandler.change_response = {"execution_id": "exec-test", "verified": False, "committed": True, "state": "failed"}
        with tempfile.TemporaryDirectory() as directory:
            content_file = Path(directory) / "desired.txt"
            content_file.write_text("new contents", encoding="utf-8")
            code, output, errors = self.run_client(content_file)

        self.assertEqual(code, 1)
        self.assertIn("did not confirm ackOS verification and commitment", errors)
        self.assertNotIn("verified and committed", output)

    def test_rejects_parent_traversal_before_network_call(self):
        with tempfile.TemporaryDirectory() as directory:
            content_file = Path(directory) / "desired.txt"
            content_file.write_text("new contents", encoding="utf-8")
            env = {
                "ACKOS_API_BASE_URL": self.base_url,
                "ACKOS_API_BEARER_TOKEN": "test-secret",
                "ACKOS_API_REPOSITORY_ID": "disposable",
            }
            with patch.dict(os.environ, env, clear=False), contextlib.redirect_stderr(io.StringIO()):
                code = ackos_api_change.main([
                    "--branch", "test-branch",
                    "--path", "../outside",
                    "--content-file", str(content_file),
                ])
        self.assertEqual(code, 1)
        self.assertEqual(FakeAPIHandler.requests, [])


if __name__ == "__main__":
    unittest.main()
