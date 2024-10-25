#!/usr/bin/env python3
"""Module for caching system with Redis"""

import uuid
from functools import wraps
from typing import Callable, Optional, Union
import redis


def log_call_history(method: Callable) -> Callable:
    """
    Decorator to log inputs and outputs of a method to Redis.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Stores method call inputs and outputs."""
        method_name = method.__qualname__
        self._redis.rpush(f"{method_name}:inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(f"{method_name}:outputs", result)
        return result

    return wrapper


def display_call_history(method: Callable) -> None:
    """
    Prints the history of inputs and outputs for a method stored in Redis.
    """
    method_name = method.__qualname__
    redis_store = method.__self__._redis
    inputs = redis_store.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_store.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for inp, outp in zip(inputs, outputs):
        inp = inp.decode("utf-8")
        outp = outp.decode("utf-8")
        print(f"{method_name}(*{inp}) -> {outp}")


def count_method_calls(method: Callable) -> Callable:
    """
    Decorator to keep track of how many times a method is invoked.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increases call count on each invocation."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Cache class that interacts with Redis for storing and retrieving data.
    """

    def __init__(self, flush_db: bool = True) -> None:
        """
        Initializes Redis connection. Optionally flushes database on start.
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        if flush_db:
            self._redis.flushdb()

    @log_call_history
    @count_method_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Saves data in Redis using a randomly generated UUID as the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieves data from Redis at the given key, optionally transforming it using a function `fn`.
        """
        value = self._redis.get(key)
        if value is not None and fn:
            value = fn(value)
        return value

    def get_as_int(self, key: str) -> Optional[int]:
        """
        Retrieves the value at `key` and converts it to an integer if found.
        """
        return self.get(key, int)

    def get_as_str(self, key: str) -> Optional[str]:
        """
        Retrieves the value at `key` and converts it to a string if found.
        """
        return self.get(key, str)

