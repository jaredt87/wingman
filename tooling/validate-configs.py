#!/usr/bin/env python3
"""Validate checked-in team metadata and runtime-config examples against JSON Schema."""
from pathlib import Path
import sys
import json
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    (ROOT / "team.yaml", ROOT / "schemas/team.schema.json"),
    (ROOT / "examples/brain.config.example.yaml", ROOT / "schemas/brain-config.schema.json"),
]
# Validate the generated root runtime config when a team checks it in.
ROOT_RUNTIME_CONFIG = ROOT / "brain.config.yaml"
if ROOT_RUNTIME_CONFIG.is_file():
    CASES.append((ROOT_RUNTIME_CONFIG, ROOT / "schemas/brain-config.schema.json"))

def main() -> int:
    failures = 0
    for data_path, schema_path in CASES:
        with data_path.open(encoding="utf-8") as stream:
            data = yaml.safe_load(stream)
        with schema_path.open(encoding="utf-8") as stream:
            schema = json.load(stream)
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(map(str, e.path)))
        if errors:
            failures += len(errors)
            for error in errors:
                location = ".".join(map(str, error.absolute_path)) or "<root>"
                print(f"ERROR {data_path.relative_to(ROOT)}:{location}: {error.message}")
        else:
            print(f"OK {data_path.relative_to(ROOT)} conforms to {schema_path.relative_to(ROOT)}")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
