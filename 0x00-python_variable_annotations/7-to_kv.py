#!/usr/bin/env python3
"""Defines complex types string, int and float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function takes a str and int and returns a str or float tuple"""
    return (str(k), (v * v))
