from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("Usage: python restore_document.py <document_name>")
    sys.exit(1)

document_name = sys.argv[1]

archive = Path("archive")

matches = list(archive.rglob(f"{document_name}.md"))

if len(matches) == 0:
    print(f"ERROR: '{document_name}.md' not found.")
    sys.exit(1)

if len(matches) > 1:
    print("ERROR: Multiple documents found:")
    for file in matches:
        print(file)
    sys.exit(1)

print("Archived document found:")
print(matches[0])
