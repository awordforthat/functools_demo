import functools


@functools.lru_cache(maxsize=5)
def factorial(n):
    print("Called with", n)
    return n * factorial(n - 1) if n else 1


factorial(6)
print(factorial.cache_info())
assert factorial.cache_info().hits == 0
assert factorial.cache_info().misses == 7

factorial(3)
print(factorial.cache_info())
# assert factorial.cache_info().hits == 1
# assert factorial.cache_info().misses == 18

# assert factorial.cache_info().hits == 0
# assert factorial.cache_info().misses == 6
