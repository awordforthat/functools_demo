import functools


def multiply_evens(current_value: int, next_value: int):
    return current_value * (next_value if next_value % 2 == 0 else 1)


integers = [1, 2, 3, 4, 5, 6]
empty = []

integers_result = functools.reduce(multiply_evens, integers)
empty_result = functools.reduce(multiply_evens, empty, 1)

assert integers_result == 48
assert empty_result == 1
