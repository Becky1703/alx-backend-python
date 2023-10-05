#!/usr/bin/env python3
"""Defines a complex list type"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function takes a list of integers and floats and returns their sum
    as float"""
    return float(sum(mxd_list))
