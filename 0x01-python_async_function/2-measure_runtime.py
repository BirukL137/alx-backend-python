#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns total_time / n.

    Args:
        n (int): Number of times to spawn the wait_random coroutine.
        max_delay (int): Maximum delay in seconds for each wait_random
        coroutine.

    Returns:
        float: Average execution time for each coroutine.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
