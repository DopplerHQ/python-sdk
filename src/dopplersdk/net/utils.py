"""
Helper functions for http calls.

Functions:
    to_serialize
"""

import io
from enum import Enum


def to_serialize(obj):
    """
    Recursively converts objects into dictionaries.

    Parameters:
    ----------
        obj:
            The object to transform into a dictionary.
    """
    result = {}
    if not hasattr(obj, "__dict__") or isinstance(
        obj, (io.TextIOWrapper, io.BufferedIOBase)
    ):
        return obj
    iter_obj = obj.__dict__.items() if hasattr(obj, "__dict__") else obj.items()
    for key, value in iter_obj:
        if isinstance(value, (io.TextIOWrapper, io.BufferedIOBase)):
            result[key] = value
        if isinstance(value, Enum):
            result[key] = value.value
        elif hasattr(value, "__dict__"):
            result[key] = to_serialize(value)
        else:
            result[key] = value
    return result
