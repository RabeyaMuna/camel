"""Compatibility shim for the deprecated ``datacommons_pandas`` package."""

from __future__ import annotations

from typing import Any

try:
    import datacommons_client as _dc_client
except ImportError as exc:  # pragma: no cover - import error is user-facing
    raise ImportError(
        "datacommons-client is required for Data Commons support."
    ) from exc

_CLIENT_PACKAGE = _dc_client


def get_stat_series(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError(
        "`datacommons_pandas.get_stat_series` is not available via the "
        "compatibility shim. Migrate this call to `datacommons_client`."
    )
