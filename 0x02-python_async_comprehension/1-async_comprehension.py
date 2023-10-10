#!/usr/bin/env python3
"""Asynchronous Comprehension"""
import asyncio
import random
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """function takes 10 random numbers using an async comprehension
    and returns 10 random numbers"""
    return [num async for num in async_generator()]
