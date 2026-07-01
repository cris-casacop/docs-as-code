from pathlib import Path


def is_internal_link(target: str) -> bool:
    """
    Returns True if the target is a local file.
    """

    if target.startswith("http://"):
        return False

    if target.startswith("https://"):
        return False

    if target.startswith("mailto:"):
        return False

    if target.startswith("#"):
        return False

    return True


def validate_internal_link(document: Path, target: str):

    destination = (document.parent / target).resolve()

    return destination.exists()
