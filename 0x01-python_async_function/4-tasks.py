#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The function returns results in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds for each task.
    
    Returns:
        List[float]: List of the dalays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delay1 = await asyncio.gather(*tasks)
    return sorted(delay1)
