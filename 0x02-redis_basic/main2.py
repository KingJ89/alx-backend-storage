#!/usr/bin/env python3
""" Main script to test Cache class with inputs and outputs history """

# Import the Cache class from the exercise module
Cache = __import__('exercise').Cache

# Instantiate a Cache object
cache = Cache()

# Store three items in the cache and print their unique keys
s1 = cache.store("first")
print(f"Key for 'first': {s1}")
s2 = cache.store("second")
print(f"Key for 'second': {s2}")
s3 = cache.store("third")
print(f"Key for 'third': {s3}")

# Retrieve and display the history of inputs and outputs for the store method
inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

# Decode bytes to strings for readability
decoded_inputs = [input.decode("utf-8") for input in inputs]
decoded_outputs = [output.decode("utf-8") for output in outputs]

print("Inputs:", decoded_inputs)
print("Outputs:", decoded_outputs)

