from pathlib import Path

docs = Path("docs")

documents = sorted(docs.rglob("*.md"))

print("Scanning documentation...\n")

for document in documents:
    print(document)

print(f"\nDocuments scanned: {len(documents)}")
