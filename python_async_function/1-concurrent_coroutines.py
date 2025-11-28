#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """
import asyncio
from typing import List
import random

# import edirik
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that returns the list of results from n coroutines

    Args:
        n (int): Number of coroutines to run
        max_delay (int): Maximum delay for wait_random

    Returns:
        List[float]: List of returned float values
    """
    # create tasks
    l = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    # await their completion as they finish
    finish = [await task for task in asyncio.as_completed(l)]
    return finish
