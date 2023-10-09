#!/usr/bin/env python3
""" Asynchronous Coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asyncronous function that takes an intger argument and waits for
    a random delay"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
