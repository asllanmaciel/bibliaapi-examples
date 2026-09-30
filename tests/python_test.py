from __future__ import annotations

import importlib.util
import io
import os
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

MODULE_PATH = Path(__file__).parents[1] / "examples" / "python" / "get_verse.py"
SPEC = importlib.util.spec_from_file_location("bibliaapi_python_example", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FakeResponse:
    def __init__(self, body: bytes, status: int = 200):
        self._body = body
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self) -> bytes:
        return self._body


class BibliaApiPythonExampleTest(unittest.TestCase):
    def test_requires_token_from_environment(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(
                RuntimeError, "Defina BIBLIA_API_TOKEN antes de executar"
            ):
                MODULE.require_token()

    def test_sends_bearer_token_and_timeout(self):
        captured = {}

        def opener(request, timeout):
            captured["authorization"] = request.get_header("Authorization")
            captured["accept"] = request.get_header("Accept")
            captured["timeout"] = timeout
            return FakeResponse(b'{"reference":"Jo 3:16"}')

        payload = MODULE.fetch_verse("test-token", opener=opener)

        self.assertEqual({"reference": "Jo 3:16"}, payload)
        self.assertEqual("Bearer test-token", captured["authorization"])
        self.assertEqual("application/json", captured["accept"])
        self.assertEqual(10, captured["timeout"])

    def test_http_error_does_not_expose_token_or_response_body(self):
        secret = "super-secret-token"

        def opener(request, timeout):
            raise HTTPError(
                MODULE.URL,
                401,
                "Unauthorized",
                hdrs=None,
                fp=io.BytesIO(b'{"debug":"super-secret-token"}'),
            )

        with self.assertRaises(RuntimeError) as raised:
            MODULE.fetch_verse(secret, opener=opener)

        message = str(raised.exception)
        self.assertEqual("A API respondeu com HTTP 401.", message)
        self.assertNotIn(secret, message)
        self.assertNotIn("debug", message)

    def test_rejects_malformed_json_without_echoing_body(self):
        def opener(request, timeout):
            return FakeResponse(b"<html>sensitive upstream body</html>")

        with self.assertRaises(RuntimeError) as raised:
            MODULE.fetch_verse("test-token", opener=opener)

        message = str(raised.exception)
        self.assertEqual("A API respondeu com JSON inválido.", message)
        self.assertNotIn("sensitive upstream body", message)

    def test_rejects_non_2xx_response_object(self):
        def opener(request, timeout):
            return FakeResponse(b'{"error":"unavailable"}', status=503)

        with self.assertRaisesRegex(RuntimeError, "HTTP 503"):
            MODULE.fetch_verse("test-token", opener=opener)


if __name__ == "__main__":
    unittest.main()
