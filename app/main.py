from functools import wraps
from typing import Callable


def is_inmutable(*arg) -> bool:
    return isinstance(arg, (int, float, complex, str, tuple, frozenset, bytes))
    """Check if argument is inmutable."""


def cache(func: Callable) -> Callable:
    store = {}  # Contains cached results

    @wraps(func)
    def inner(*args, **kwargs) -> None:

        if not all(is_inmutable(arg) for arg in args):
            return func(*args, **kwargs)

        key = (args, frozenset(kwargs.items()))

        if key in store:
            print("Getting from cache")
            return store.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            store[key] = result
            return result
    return inner
