#!/usr/bin/env python3
"""
Complex types - functions
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): A float number to multiply with.

    Returns:
        Callable: A function that takes a float number and
        returns the product of the input and multiplier.
    """
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
