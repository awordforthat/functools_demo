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


def report_status(message):
    print(message)


beginning_callback = {
    "time": 0,
    "function": functools.partial(report_status, "Timer has started"),
    "id": "beginning",
}

middle_callback = {
    "time": 1,
    "function": functools.partial(report_status, "One second has passed"),
    "id": "one_second",
}


end_callback = {
    "time": 2,
    "function": functools.partial(report_status, "Timer is complete"),
    "id": "end",
}

timer = BlockingTimer(3, [beginning_callback, middle_callback, end_callback])
timer.start()
