#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function returns a list of tuples where each tuple contains
    an element from the input list and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
