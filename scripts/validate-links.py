from pathlib import Path

from validators.markdown import extract_links
from validators.internal_links import (
    is_internal_link,
    validate_internal_link,
)

docs = Path("docs")

documents = sorted(docs.rglob("*.md"))

total_documents = 0
total_links = 0
broken_links = 0

print(f"Scanning {len(documents)} documents...\n")

for document in documents:

    total_documents += 1

    print(f"{document}")

    links = extract_links(document)

    if not links:
        print("  No links found.\n")
        continue

    for link in links:

        target = link["target"]
        total_links += 1

        if not is_internal_link(target):
            print(f"  SKIP   {target}")
            continue

        if validate_internal_link(document, target):
            print(f"  OK     {target}")
        else:
            print(f"  BROKEN {target}")
            broken_links += 1

    print()

print("----------------------------------------")
print(f"Documents scanned : {total_documents}")
print(f"Links discovered  : {total_links}")
print(f"Broken links      : {broken_links}")

if broken_links > 0:
    raise SystemExit(1)

print("\nValidation passed.")
