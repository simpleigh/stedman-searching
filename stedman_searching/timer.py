from time import perf_counter


class Timer:
    def __init__(self):
        self._time = perf_counter()

    def split(self):
        new_time = perf_counter()
        elapsed_time = new_time - self._time
        self._time = new_time
        return elapsed_time
