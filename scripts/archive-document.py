from pathlib import Path
from datetime import date
import shutil
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python archive_document.py <document_name>")
    sys.exit(1)

document_name = sys.argv[1]

docs = Path("docs")
archive = Path("archive")

matches = list(docs.rglob(f"{document_name}.md"))

if len(matches) == 0:
    print(f"ERROR: '{document_name}.md' not found.")
    sys.exit(1)

if len(matches) > 1:
    print("ERROR: Multiple documents found:")
    for file in matches:
        print(file)
    sys.exit(1)

source = matches[0]

# Preserve the folder structure under archive/
relative_path = source.relative_to(docs)
destination = archive / relative_path

# Create archive directory if needed
destination.parent.mkdir(parents=True, exist_ok=True)

# Read document
content = source.read_text(encoding="utf-8")

today = date.today().isoformat()

# Update status
content = re.sub(
    r"^status:\s*.*",
    "status: Archived",
    content,
    flags=re.MULTILINE
)

# Update last_updated
content = re.sub(
    r"^last_updated:\s*.*",
    f"last_updated: {today}",
    content,
    flags=re.MULTILINE
)

# Update updated_by
content = re.sub(
    r"^updated_by:\s*.*",
    "updated_by: github-actions",
    content,
    flags=re.MULTILINE
)

# Increment version
match = re.search(r"^version:\s*(\d+)\.(\d+)", content, re.MULTILINE)

if match:
    major = int(match.group(1))
    minor = int(match.group(2)) + 1
    new_version = f"{major}.{minor}"

    content = re.sub(
        r"^version:\s*\d+\.\d+",
        f"version: {new_version}",
        content,
        flags=re.MULTILINE
    )

# Write archived document
destination.write_text(content, encoding="utf-8")

# Remove original
source.unlink()

print(f"Archived: {destination}")
