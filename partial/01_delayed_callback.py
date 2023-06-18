"""
In this exercise, you will write a function that calls another after a delay.

You should fill in the body of `call_after_delay` with two arguments:
    - the first argument should be positional, and should be the current time (use `time.monotonic`)
    - the second argument should be a keyword argument, and should be the time in seconds 
        that the program should delay. Use `time.sleep` to implement the delay.

You should also fill in the value of `call_later` with a call to functools.partial, including the arguments
as described above.

When you have made the changes above, this script should complete with no assertion errors.
"""

import functools
import time


def call_after_delay(*args, **kwargs):
    pass


delay_seconds = 3
now = time.monotonic()

call_later = None  # Replace 'None' with a call to functools.partial
time_delta = call_later()

assert time_delta >= delay_seconds
