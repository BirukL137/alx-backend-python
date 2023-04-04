#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The function coroutine loops 10 times and each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.

    Returns:
        Generator (float): lists 10 generated random float numbers
        between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
