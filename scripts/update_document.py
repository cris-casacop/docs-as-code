from pathlib import Path
from datetime import date
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python update_document.py <document_name>")
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

print(f"Updating: {file}")

content = file.read_text(encoding="utf-8")

today = date.today().isoformat()

# Update last_updated
content = re.sub(
    r"last_updated:\s*.*",
    f"last_updated: {today}",
    content
)

# Update updated_by
content = re.sub(
    r"updated_by:\s*.*",
    f"updated_by: github-actions",
    content
)

# Increment version
match = re.search(r"version:\s*(\d+)\.(\d+)", content)

if match:
    major = int(match.group(1))
    minor = int(match.group(2)) + 1

    new_version = f"{major}.{minor}"

    content = re.sub(
        r"version:\s*\d+\.\d+",
        f"version: {new_version}",
        content
    )

else:
    print("Version not found. Adding version: 1.0")

    content = content.replace(
        "---",
        "version: 1.0\n---",
        1
    )

file.write_text(content, encoding="utf-8")

print("Metadata updated successfully.")
