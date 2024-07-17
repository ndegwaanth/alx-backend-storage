#!/usr/bin/env python3
"""sample python redis implementation module"""
import redis
import uuid
from typing import Callable, Union, Any
from functools import cache, wraps


def count_calls(method: Callable) -> Callable:
    """wrapper around Cache.store method
    Args:
        method-> function wrapped around this function
    Return:
        the calling method but first sets/increments the number
        of times the function is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """implements the wrapping functionality
        https://docs.python.org/3.7/library/functools.html#functools.wraps
        """
        key = method.__qualname__
        if self._redis.get(key) is None:
            self._redis.set(key, 1)
        else:
            self._redis.incr(key, 1)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    function that the decorator will return,
    use rpush to append the input arguments
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_keys = "{}:inputs".format(method.__qualname__)
        output_keys = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(input_keys, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_keys, str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    display the history of calls of a particular function.
    """
    input_keys = "{}:inputs".format(method.__qualname__)
    output_keys = "{}:outputs".format(method.__qualname__)
    inputs = cache._redis.lrange(
            "{}:inputs".format(cache.store.__qualname__), 0, -1)
    outputs = cache._redis.lrange(
            "{}:outputs".format(cache.store.__qualname__), 0, -1)
    values = dict(zip(inputs, outputs))
    times = cache.get(cache.store.__qualname__)
    print("Cache.store was called {} times:".format(times.decode('utf-8')))
    for key, value in values.items():
        print("Cache.store(*{}) -> {}".format(
            key.decode('utf-8'), value.decode('utf-8')))


class Cache():
    """redis class"""
    def __init__(self):
        """initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """store the data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        self._redis.rpush(':inputs', str(data))
        self._redis.rpush(':outputs', key)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[int, str, None]:
        """get the element of the key"""
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, val: str) -> Union[str, None]:
        """convert to string"""
        return str(val)

    def get_int(self, val: str) -> Union[int, None]:
        """covert to int"""

        return int(val)
