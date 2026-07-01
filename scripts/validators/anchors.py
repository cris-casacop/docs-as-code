import re
from pathlib import Path


def slugify(heading: str) -> str:
    """
    Convert a Markdown heading into a GitHub anchor.

    Example:
        ## Validation Process
            ↓
        validation-process
    """

    heading = heading.strip().lower()

    heading = re.sub(r"[^\w\s-]", "", heading)

    heading = re.sub(r"\s+", "-", heading)

    return heading


def get_anchors(markdown_file: Path):

    content = markdown_file.read_text(encoding="utf-8")

    anchors = set()

    for line in content.splitlines():

        if line.startswith("#"):

            heading = line.lstrip("#").strip()

            anchors.add(slugify(heading))

    return anchors


def validate_anchor(markdown_file: Path, anchor: str):

    anchors = get_anchors(markdown_file)

    return anchor in anchors
