#!/usr/bin/env python3
"""Asynchronous function"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates an asynchronous task"""
    return asyncio.create_task(wait_random(max_delay))
