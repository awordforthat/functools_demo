import functools


@functools.cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


factorial(10)
assert factorial.cache_info().hits == 0
assert factorial.cache_info().misses == 11

factorial(17)
assert factorial.cache_info().hits == 1
assert factorial.cache_info().misses == 18

factorial.cache_clear()
factorial(5)
assert factorial.cache_info().hits == 0
assert factorial.cache_info().misses == 6
