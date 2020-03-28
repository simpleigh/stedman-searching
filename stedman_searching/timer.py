from time import perf_counter


class Timer:
    """
    A simple timer for profiling

    Starts counting once instantiated, and resets at each call to `split()`.
    """

    def __init__(self):
        self._time = perf_counter()

    def split(self):
        """ Returns the elapsed time and then resets the timer """
        new_time = perf_counter()
        elapsed_time = new_time - self._time
        self._time = new_time
        return elapsed_time
