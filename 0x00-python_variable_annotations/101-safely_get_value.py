#!/usr/bin/env python3
"""Type Annotation"""
from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
