from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import ssl

TIMEOUT = 10


def is_external_link(target: str) -> bool:
    """
    Returns True if the target is an HTTP or HTTPS URL.
    """
    return target.startswith("http://") or target.startswith("https://")


def validate_external_link(url: str):
    """
    Validate an external URL.

    Returns:
        (passed, message)
    """

    try:
        request = Request(
            url,
            headers={
                "User-Agent": "Docs-as-Code Link Validator/1.0"
            }
        )

        with urlopen(request, timeout=TIMEOUT) as response:
            status = response.getcode()

            if 200 <= status < 400:
                return True, f"HTTP {status}"

            return False, f"HTTP {status}"

    except HTTPError as e:
        return False, f"HTTP {e.code}"

    except URLError as e:
        return False, f"URL Error: {e.reason}"

    except ssl.SSLError:
        return False, "SSL Error"

    except Exception as e:
        return False, str(e)
