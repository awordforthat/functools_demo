"""
This example demonstrates how you might use `functools.partial` to consolidate callbacks 
from a running timer. (Note that the timer is kind of naively implemented, and is custom-written
to make it suitable for this example). 

The BlockingTimer will run for a given duration and call any callbacks at their designated times.
Callbacks are provided as dictionaries with three keys: a `time` in seconds at which the callback
should be invoked, a `function` that should be called, and a unique `id`, which you can ignore. For
this example, you don't need to touch the BlockingTimer code at all.

The script defines three callbacks, each with its own designated function. We can make this code
shorter and more flexible using `functools.partial`. 

First, define a method `report_status`. It should take just one argument and print it out to the console.

Next, for each callback, replace the "function" item in the dictionary with a call to `functools.partial`. 
Use the "report_status" function you just defined as part of that call.

There are no assertions for this example, but your solution should replicate the current behavior:
    - At time 0, it prints "Timer has started"
    - At 1 second, it prints "One second has passed"
    - When the timer is complete, it prints "Timer is complete"
"""

import functools
import time


class BlockingTimer:
    """
    This timer has some features that make it unsuitable for production.
    You probably shouldn't use it for anything important!
    """

    def __init__(self, duration, callbacks):
        self.duration = duration
        self.running = False
        self.callbacks = callbacks

    def start(self):
        start_time = time.monotonic()
        while time.monotonic() - start_time <= self.duration:
            now = time.monotonic()
            elapsed = now - start_time
            callbacks_to_remove: list = []
            for callback in self.callbacks:
                if callback.get("time") <= elapsed:
                    callback.get("function")()
                    callbacks_to_remove.append(callback.get("id"))
            self.callbacks = list(
                filter(
                    lambda cb: cb.get("id") not in callbacks_to_remove, self.callbacks
                )
            )
            time.sleep(0.1)
        # any callbacks left over are called at the very end
        for callback in self.callbacks:
            callback.get("function")()


def report_start():
    print("Timer has started")


def report_middle():
    print("One second has passed")


def report_end():
    print("Timer is complete")


beginning_callback = {
    "time": 0,
    "function": report_start,
    "id": "beginning",
}

middle_callback = {
    "time": 1,
    "function": report_middle,
    "id": "one_second",
}


end_callback = {
    "time": 2,
    "function": report_end,
    "id": "end",
}

timer = BlockingTimer(2, [beginning_callback, middle_callback, end_callback])
timer.start()
