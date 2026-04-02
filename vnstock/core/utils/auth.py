# vnstock/core/utils/auth.py

"""
User authentication and API key registration for vnstock.

NOTE: This module requires the 'vnai' package which has been removed.
Functions will return appropriate messages indicating vnai is not available.
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)

_VNAI_REMOVED_MSG = (
    "vnai module has been removed from this installation. "
    "API key registration and tier management are not available."
)


def register_user(api_key: Optional[str] = None) -> bool:
    """
    User registration with optional API key parameter.

    NOTE: Requires vnai package which has been removed.

    Args:
        api_key: Optional API key to register directly

    Returns:
        bool: Always False (vnai removed)
    """
    print(f"✗ {_VNAI_REMOVED_MSG}")
    return False


def change_api_key(api_key: str) -> bool:
    """
    Change API key directly.

    NOTE: Requires vnai package which has been removed.

    Args:
        api_key: New API key

    Returns:
        bool: Always False (vnai removed)
    """
    print(f"✗ {_VNAI_REMOVED_MSG}")
    return False


def check_status() -> Optional[dict]:
    """
    Check current registration status.

    NOTE: Requires vnai package which has been removed.

    Returns:
        dict: Status information indicating vnai is not available
    """
    print(f"✗ {_VNAI_REMOVED_MSG}")
    return {
        "has_api_key": False,
        "api_key_preview": None,
        "tier": "unlimited",
        "limits": {"per_minute": "unlimited", "per_hour": "unlimited"},
        "note": "vnai removed - no rate limiting applied",
    }
