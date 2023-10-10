#!/usr/bin/env python3
"""Asynchronous Comprehension"""
import asyncio
import random
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function takes 10 random numbers using an async comprehension
    and returns 10 random numbers"""
    return [num async for num in async_generator()]
