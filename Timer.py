import time
from threading import Thread, Event


class Timer(Thread):
    interval = None

    def __init__(self):
        self._timer_runs = Event()
        self._timer_runs.set()
        super().__init__()

    def run(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval)

    def stop(self):
        self._timer_runs.clear()

    def timer(self):
        pass
