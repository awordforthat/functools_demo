"""
For this exercise, your goal is to recreate the basic functionality of `functools.cache` 
by defining your own cache decorator. 

Your decorator should call the wrapped function only if the arguments given do not 
exist in the cache yet. If the arguments do exist in the cache, return that value instead.

For bonus points, you can try implementing this with a CacheInfo object as well!
"""


def diy_cache(func):
    pass


@diy_cache
def factorial(n):
    return n * factorial(n - 1) if n else 1
