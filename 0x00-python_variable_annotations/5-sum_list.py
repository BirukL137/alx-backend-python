#!/usr/bin/env python3
"""
Complex types - list of floats
"""


def sum_list(input_list: list[float]) -> float:
    """
    This function takes a list of floats as input
    and returns their sum as a float.

    Args:
        input_list (list[float]): A list of floats.

    Returns:
        float: The sum of the input list.

    Example:
    >>> sum_list([1.0, 2.0, 3.0])
    6.0
    """
    return sum(input_list)
