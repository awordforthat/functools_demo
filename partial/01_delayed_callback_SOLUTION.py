import functools
import time


def get_time_delta(*args):
    return time.monotonic() - args[0]


now = time.monotonic()
call_later = functools.partial(get_time_delta, time.monotonic())
time.sleep(1)
time_delta = call_later()

assert time_delta >= 1
