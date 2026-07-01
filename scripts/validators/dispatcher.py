from pathlib import Path

from validators.internal_links import is_internal_link, validate_internal_link
from validators.anchors import validate_anchor


def validate_reference(document: Path, target: str):
    """
    Route a Markdown reference to the correct validator.
    Returns:
        tuple[bool, str]
    """

    if target.startswith("#"):
        anchor = target[1:]

        if validate_anchor(document, anchor):
            return True, "anchor valid"

        return False, "anchor not found"

    if is_internal_link(target):
        if validate_internal_link(document, target):
            return True, "internal file exists"

        return False, "internal file not found"

    return True, "skipped"
