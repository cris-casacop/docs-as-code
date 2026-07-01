from pathlib import Path

from validators.markdown import extract_links

docs = Path("docs")

documents = sorted(docs.rglob("*.md"))

print(f"Scanning {len(documents)} documents...\n")

total_links = 0

for document in documents:

    print(f"\n{document}")

    links = extract_links(document)

    if not links:
        print("  No links found.")
        continue

    for link in links:
        print(f"  {link['target']}")

    total_links += len(links)

print("\n--------------------------------")

print(f"Documents scanned : {len(documents)}")
print(f"Links discovered  : {total_links}")
