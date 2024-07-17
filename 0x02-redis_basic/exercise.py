import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.
        Args:
            data: union of data types[str,bytes,int,float]
            data to be stored
            Returns: the randomly generated keys
        """
        key = str(uuid.uuid4)
        self._redis.set(key, data)
        return key
