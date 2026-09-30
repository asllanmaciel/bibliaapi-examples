#!/usr/bin/env python3
"""Minimal, dependency-free BIBLIAAPI example using Python's standard library."""

from __future__ import annotations

import json
import os
import sys
from json import JSONDecodeError
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

URL = "https://bibliaapi.com.br/api/v2/versions/acf/books/jo/chapters/3/verses/16"
TIMEOUT_SECONDS = 10


def require_token() -> str:
    token = os.environ.get("BIBLIA_API_TOKEN", "")
    if not token:
        raise RuntimeError("Defina BIBLIA_API_TOKEN antes de executar.")
    return token


def fetch_verse(token: str, opener=urlopen) -> object:
    request = Request(
        URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        },
        method="GET",
    )

    try:
        with opener(request, timeout=TIMEOUT_SECONDS) as response:
            status = getattr(response, "status", 200)
            raw_body = response.read()
    except HTTPError as error:
        raise RuntimeError(f"A API respondeu com HTTP {error.code}.") from None
    except (URLError, TimeoutError, OSError) as error:
        reason = getattr(error, "reason", str(error))
        raise RuntimeError(
            f"Não foi possível conectar à BIBLIAAPI: {reason}."
        ) from None

    if not 200 <= status < 300:
        raise RuntimeError(f"A API respondeu com HTTP {status}.")

    try:
        return json.loads(raw_body.decode("utf-8"))
    except (UnicodeDecodeError, JSONDecodeError):
        raise RuntimeError("A API respondeu com JSON inválido.") from None


def main() -> int:
    try:
        data = fetch_verse(require_token())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1

    print(json.dumps(data, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
