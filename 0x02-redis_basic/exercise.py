import redis
import uuid
import functools
from typing import Callable, Optional, Union


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

    def get(self, key: str) -> Optional[Union[str, bytes]]:
        """
        Retrieve the value from Redis using the provided key.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[Union[str, bytes]]: The retrieved value or None if the key
            does not exist.
        """
        return self._redis.get(key)


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method of Cache class is called.
    Uses Redis to store and increment the call count.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: Decorated function that increments the count and calls the
                  original method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        count_key = f"method_calls:{method.__qualname__}"
        self._redis.incr(count_key)
        return method(self, *args, **kwargs)

    return wrapper


# Applying the decorator to the store method of Cache
Cache.store = count_calls(Cache.store)
