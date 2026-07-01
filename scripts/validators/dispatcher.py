from pathlib import Path

from validators.internal_links import (
    is_internal_link,
    validate_internal_link,
)

from validators.anchors import validate_anchor

from validators.external_links import (
    is_external_link,
    validate_external_link,
)


def validate_reference(document: Path, target: str):
    """
    Route a Markdown reference to the correct validator.

    Returns:
        (passed, message)
    """

    # Same-document anchor
    if target.startswith("#"):

        anchor = target[1:]

        if validate_anchor(document, anchor):
            return True, "anchor valid"

        return False, "anchor not found"

    # External HTTP/HTTPS
    if is_external_link(target):
        return validate_external_link(target)

    # Internal repository file
    if is_internal_link(target):

        if validate_internal_link(document, target):
            return True, "internal file exists"

        return False, "internal file not found"

    # Ignore everything else for now
    return True, "skipped"
