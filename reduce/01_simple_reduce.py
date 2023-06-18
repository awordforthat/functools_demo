"""
For this exercise, you will need to use the `multiply_evens` function along with `functools.reduce`.

Write expressions for `integers_result` and `empty_result` such that both assertions below pass.
"""


import functools


def multiply_evens(current_value: int, next_value: int):
    """
    This function multiplies the current value by the incoming value if and only if the incoming
    value is even.
    """
    return current_value * (next_value if next_value % 2 == 0 else 1)


integers = [1, 2, 3, 4, 5, 6]
empty = []

integers_result = False  # Replace 'False' using functools.reduce
empty_result = False  # Replace 'False' using functools.reduce

assert integers_result == 48
assert empty_result == 1
