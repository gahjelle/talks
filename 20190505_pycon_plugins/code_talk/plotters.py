"""Plot Pandas DataFrames"""

# Third party imports

_PLOTTERS = dict()


def register(func):
    _PLOTTERS[func.__name__] = func
    return func


def plot(plugin, *args, **kwargs):
    if plugin in _PLOTTERS:
        return _PLOTTERS[plugin](*args, **kwargs)
    else:
        raise TypeError(f"{plugin} not available")
