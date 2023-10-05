#!/usr/bin/env python3
"""Defines complex types -List of Floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function takes a list of floats and returns their sum as a float"""
    return float(sum(input_list))
