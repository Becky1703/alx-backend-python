#!/usr/bin/env python3
"""Complex type - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function takes a float as argument and returns a function that
    multiplies a float by the argument"""
    return lambda x: x * multiplier
