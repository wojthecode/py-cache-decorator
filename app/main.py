from functools import wraps
from typing import Callable, Any


def is_inmutable(value: Any) -> bool:
    return isinstance(value, (int, float, complex, str,
                              tuple, frozenset, bytes))
    """Check if argument is inmutable."""


def cache(func: Callable) -> Callable:
    store = {}  # Contains cached results

    @wraps(func)
    def inner(*args, **kwargs) -> Any:

        key = args + tuple(sorted(kwargs.items()))

        if not all(is_inmutable(value)for value in key):
            print("Argument is mutable, won't be cached")
            return None

        if key in store:
            print("Getting from cache")
            return store.get(key)
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            store[key] = result
            return result
    return inner
