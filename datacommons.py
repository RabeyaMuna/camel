"""Compatibility shim for the deprecated ``datacommons`` package.

This project historically imported the V1 ``datacommons`` module directly.
The upstream package is now yanked from PyPI in favor of
``datacommons-client``. This shim keeps imports and tests working while the
toolkit migrates to the V2 client API.
"""

from __future__ import annotations

from typing import Any

try:
    import datacommons_client as _dc_client
except ImportError as exc:  # pragma: no cover - import error is user-facing
    raise ImportError(
        "datacommons-client is required for Data Commons support."
    ) from exc

_CLIENT_PACKAGE = _dc_client


def _unsupported(name: str) -> NotImplementedError:
    return NotImplementedError(
        f"`datacommons.{name}` is not available via the compatibility shim. "
        "Migrate this call to `datacommons_client`."
    )


def query(*args: Any, **kwargs: Any) -> Any:
    raise _unsupported("query")


def get_triples(*args: Any, **kwargs: Any) -> Any:
    raise _unsupported("get_triples")


def get_property_labels(*args: Any, **kwargs: Any) -> Any:
    raise _unsupported("get_property_labels")


def get_property_values(*args: Any, **kwargs: Any) -> Any:
    raise _unsupported("get_property_values")


def get_places_in(*args: Any, **kwargs: Any) -> Any:
    raise _unsupported("get_places_in")


def get_stat_value(*args: Any, **kwargs: Any) -> Any:
    raise _unsupported("get_stat_value")


def get_stat_all(*args: Any, **kwargs: Any) -> Any:
    raise _unsupported("get_stat_all")
