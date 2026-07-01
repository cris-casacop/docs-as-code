import re
from pathlib import Path

# Markdown links:
# [text](target)

LINK_PATTERN = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def extract_links(markdown_file: Path):
    """
    Extract all Markdown links from a document.

    Returns:
        list[dict]
    """

    content = markdown_file.read_text(encoding="utf-8")

    links = []

    for match in LINK_PATTERN.finditer(content):
        text = match.group(1).strip()
        target = match.group(2).strip()

        links.append({
            "text": text,
            "target": target
        })

    return links
