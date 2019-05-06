"""Read data files in different formats"""

# Standard library imports
import json as jsonlib

# Third party imports
import pandas as pd

_READERS = dict()


def register(func):
    _READERS[func.__name__] = func
    return func


def read(plugin, *args, **kwargs):
    if plugin in _READERS:
        return _READERS[plugin](*args, **kwargs)
    else:
        raise TypeError(f"{plugin} not available")


@register
def csv(file_path):
    """Read CSV file, return DataFrame"""
    return pd.read_csv(file_path)


@register
def json(file_path):
    """Read JSON file, return DataFrame"""
    json_dict = jsonlib.loads(file_path.read_text())
    return pd.DataFrame(json_dict)
