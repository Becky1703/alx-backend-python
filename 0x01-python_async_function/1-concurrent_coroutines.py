#!/usr/bin/env python3
""" Asynchronous Coroutine """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """asyncronous function that takes an intger argument and waits for
    a random delay"""
    delay = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay)
