from pathlib import Path
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python validate_document.py <document_name>")
    sys.exit(1)

document_name = sys.argv[1]

docs = Path("docs")

matches = list(docs.rglob(f"{document_name}.md"))

if len(matches) == 0:
    print(f"ERROR: '{document_name}.md' not found.")
    sys.exit(1)

if len(matches) > 1:
    print("ERROR: Multiple documents found:")
    for file in matches:
        print(file)
    sys.exit(1)

file = matches[0]

print(f"Validating: {file}")

content = file.read_text(encoding="utf-8")

required_fields = [
    "title",
    "document_type",
    "owner",
    "author",
    "status",
    "version",
    "created",
    "last_updated",
    "updated_by",
]

missing = []

for field in required_fields:
    if not re.search(rf"^{field}:", content, re.MULTILINE):
        missing.append(field)

if missing:
    print("Validation failed.")
    print("Missing fields:")
    for field in missing:
        print(f"- {field}")
    sys.exit(1)

print("All required metadata fields exist.")
print("Validation passed.")
