#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): A list of any type.

    Returns:
        Union[Any, None]: the first element of the list if it
        exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
