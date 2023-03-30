#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string k and an int OR float v as arguments
    and returns a tuple.

    Args:
        k (str): The first element of the tuple.
        v (Union[int, float]): The second element is the square of the
        int/float v and should be annotated as a float.

    Returns:
        Tuple[str, float]: Tuple consisting of k and the square of v.
    """
    return (k, v ** 2)
