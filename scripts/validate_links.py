from pathlib import Path

from validators.markdown import extract_links
from validators.dispatcher import validate_reference

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

        passed, message = validate_reference(document, target)

        if passed:
            print(f"  OK     {target} ({message})")
        else:
            print(f"  BROKEN {target} ({message})")
            broken_links += 1

    print()

print("----------------------------------------")
print(f"Documents scanned : {total_documents}")
print(f"Links discovered  : {total_links}")
print(f"Broken links      : {broken_links}")

if broken_links > 0:
    raise SystemExit(1)

print("\nValidation passed.")
