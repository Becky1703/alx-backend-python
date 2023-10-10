#!/usr/bin/env python3
"""Asynchronous Comprehension"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function measures the run time of four parallel comprehension"""
    strt_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - strt_time
