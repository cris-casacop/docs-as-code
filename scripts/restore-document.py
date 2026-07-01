from pathlib import Path
from datetime import date
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python restore_document.py <document_name>")
    sys.exit(1)

document_name = sys.argv[1]

archive = Path("archive")
docs = Path("docs")

matches = list(archive.rglob(f"{document_name}.md"))

if len(matches) == 0:
    print(f"ERROR: '{document_name}.md' not found.")
    sys.exit(1)

if len(matches) > 1:
    print("ERROR: Multiple documents found:")
    for file in matches:
        print(file)
    sys.exit(1)

source = matches[0]

# Preserve the folder structure under docs/
relative_path = source.relative_to(archive)
destination = docs / relative_path

# Create destination directory if needed
destination.parent.mkdir(parents=True, exist_ok=True)

# Read the archived document
content = source.read_text(encoding="utf-8")

today = date.today().isoformat()

# Restore status
content = re.sub(
    r"^status:\s*.*",
    "status: Active",
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

    content = re.sub(
        r"^version:\s*\d+\.\d+",
        f"version: {major}.{minor}",
        content,
        flags=re.MULTILINE
    )

# Write restored document
destination.write_text(content, encoding="utf-8")

# Remove archived copy
source.unlink()

print(f"Document restored to: {destination}")
