#!/usr/bin/env python3
"""
Tasks
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function creates an asyncio.Task to execute wait_random.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: Task object
    """
    return asyncio.create_task(wait_random(max_delay))
