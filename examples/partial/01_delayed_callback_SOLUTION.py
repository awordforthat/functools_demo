import functools
import time


def report_timedelta(*args, **kwargs):
    time.sleep(kwargs.get("delay"))
    return time.monotonic() - args[0]


delay_seconds = 3
now = time.monotonic()

call_later = functools.partial(
    report_timedelta, now, delay=delay_seconds
)  # Replace 'None' with a call to functools.partial
time_delta = call_later()

assert time_delta >= delay_seconds
