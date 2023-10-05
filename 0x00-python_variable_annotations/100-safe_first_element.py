#!/usr/bin/env python3
"""Duck Typing"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """assigning types to argument and return value"""
    if lst:
        return lst[0]
    else:
        return None
