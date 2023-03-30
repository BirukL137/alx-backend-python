#!/usr/bin/env python3
"""
Complex types - mixed list
"""

from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    This function takes a list of integers and floats as input
    and returns their sum as a float.

    Args:
        mxd_lst (List[int | float]): A list of integers and floats.

    Returns
        float: The sum of the input list.

    Example:
    >>> sum_mixed_list([1, 2.0, 3])
    6.0
    """
    return sum(mxd_lst)
