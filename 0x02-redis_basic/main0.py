#!/usr/bin/env python3
"""
Main script to demonstrate Cache class functionality
"""
import redis
from exercise import Cache  # Import Cache from the exercise module

# Instantiate Cache object
cache = Cache()

# Store data in the cache and retrieve the generated key
data = b"hello"
key = cache.store(data)
print(f"Generated key: {key}")

# Create a direct Redis connection to verify the stored data
local_redis = redis.Redis()
print(f"Stored data in Redis: {local_redis.get(key)}")
