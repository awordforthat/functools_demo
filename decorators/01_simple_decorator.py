"""
Exercise 1: fill in the body of `call_twice` so that it invokes the wrapped function twice. 
Make sure you return a function, not the result of increment()!

Run this file with `python 01_simple_decorator.py`. If your solution is correct, it should 
complete with no assertion errors.
"""


global_sum = 0  # Don't use mutable global variables 🙃


def call_twice(func):
    """
    This function returns a wrapper function that executes the passed-in function twice.
    """
    pass


@call_twice
def increment():
    """This function adds one to the global sum."""
    global global_sum
    global_sum += 1


increment()

print(global_sum)
assert global_sum == 2
