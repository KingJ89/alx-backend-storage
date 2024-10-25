#!/usr/bin/env python3
""" Main script to test Cache class and method call count """

# Import Cache class from the exercise module
Cache = __import__('exercise').Cache

# Instantiate Cache object
cache = Cache()

# Store a first item in the cache and display the count of store method calls
cache.store(b"first")
print(f"Store method call count: {cache.get(cache.store.__qualname__)}")

# Store additional items to test method call counting
cache.store(b"second")
cache.store(b"third")
print(f"Updated store method call count: {cache.get(cache.store.__qualname__)}")
