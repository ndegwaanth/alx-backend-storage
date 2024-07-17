#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """Initialize the Cache with a Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float, None]:
        """
        Retrieve the value from Redis using the provided key and apply the
        conversion function if provided.

        Args:
            key (str): The key to retrieve.
            fn (Optional[Callable]): A callable to convert the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved value or None if
            the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the value from Redis as a string.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[str]: The retrieved string value or None if the key does
            not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the value from Redis as an integer.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[int]: The retrieved integer value or None if the key does
            not exist.
        """
        return self.get(key, int)


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
