"""
In this exercise, you will write a function that returns after a delay.

First, update the value of `call_later` to be a call to `functools.partial`. Give the partial
function one positional argument, which is the current time (use the `now` variable), and
one keyword argument "delay". You can use the variable `delay_seconds` here.

You should also make two changes to the body of `report_timedelta`:
    - update the argument to time.sleep
    - update the return value to be the delta between the time the function was constructed
        to the time it returned

Lastly, fill in the value of `call_later` with a call to functools.partial that includes 

When you have made the changes above, this script should complete with no assertion errors.
"""
import functools
import time


def report_timedelta(*args, **kwargs):
    time.sleep(0)  # Replace "0" here with the delay passed in to the partial function
    return (
        time.monotonic() - 0
    )  # Replace "0" here with the value of "now" passed in to the partial function


delay_seconds = 3
now = time.monotonic()

call_later = None  # Replace 'None' with a call to functools.partial
time_delta = call_later()

assert time_delta >= delay_seconds
