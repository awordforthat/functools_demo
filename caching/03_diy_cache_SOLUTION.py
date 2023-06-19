def diy_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@diy_cache
def factorial(n):
    return n * factorial(n - 1) if n else 1
