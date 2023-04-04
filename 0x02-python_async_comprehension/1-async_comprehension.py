#!/usr/bin/env python3
"""
Async Comprehensions
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The function coroutine will collect 10 random numbers using
    comprehensing over async_generator and returns 10 random numbers

    Returns:
        result[List(float)]: lists of random float numbers generated
        from imported async_generator().
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
