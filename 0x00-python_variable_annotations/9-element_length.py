#!/usr/bin/env python3
"""Function parameters and return value types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns the length of a list of sequence"""
    return [(i, len(i)) for i in lst]
