import functools


@functools.lru_cache(maxsize=5)
def factorial(n):
    print("Called with", n)
    return n * factorial(n - 1) if n else 1


# Cache is empty

factorial(5)
print(factorial.cache_info())
assert factorial.cache_info().hits == 0
assert factorial.cache_info().misses == 6

# This is what the cache looks like at each step.
# The parameter and hit/miss value is in parentheses to the right of the cache log (N: hit/miss))

# It might seem weird that 0 is the first value in the cache even though the calls to `factorial`
# start with 5. Because `factorial` is recursive, the first value to be returned is 0 (6 levels deep in the stack).
# The last value to be returned is 5.

# [older]           [newer] <-- before any function is called
# [older] 0         [newer] (0: miss)
# [older] 0 1       [newer] (1: miss)
# [older] 0 1 2     [newer] (2: miss)
# [older] 0 1 2 3   [newer] (3: miss)
# [older] 0 1 2 3 4 [newer] (4: miss)
# [older] 1 2 3 4 5 [newer] (5: miss)

factorial(5)
print(factorial.cache_info())
assert factorial.cache_info().hits == 1
assert factorial.cache_info().misses == 6


# [older] 1 2 3 4 5 [newer] (from last step)
# [older] 1 2 3 4 5 [newer] (5: hit - 5 was already the most recent value, so the cache order doesn't change)

factorial(0)
print(factorial.cache_info())
assert factorial.cache_info().hits == 1
assert factorial.cache_info().misses == 7

# [older] 1 2 3 4 5 [newer] (from last step)
# [older] 2 3 4 5 0 [newer] (0: miss)

factorial(7)
print(factorial.cache_info())
assert factorial.cache_info().hits == 2
assert factorial.cache_info().misses == 9

# [older] 2 3 4 5 0 [newer] (from last step)
# [older] 2 3 4 0 5 [newer] (5: hit)
# [older] 3 4 0 5 6 [newer] (6: miss)
# [older] 4 0 5 6 7 [newer] (7: miss)
