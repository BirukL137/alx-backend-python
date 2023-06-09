#!/usr/bin/env python3
"""
Basic annotations - floor
"""


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Args:
        n (float): The float to take the floor of.

    Returns:
        int: The floor of the float.
    """
    return int(n) if n >= 0 else int(n) - 1
