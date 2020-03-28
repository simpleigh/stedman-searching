"""
Simple classes and functions to help with performance profiling

References:
* https://docs.python.org/3.6/library/profile.html
* https://docs.python.org/3.6/library/time.html#time.perf_counter
"""

import cProfile
import pstats
import time


class Timer:
    """
    A simple timer for profiling

    Starts counting once instantiated, and resets at each call to `split()`.
    """

    def __init__(self):
        self._time = time.perf_counter()

    def split(self):
        """ Returns the elapsed time and then resets the timer """
        new_time = time.perf_counter()
        elapsed_time = new_time - self._time
        self._time = new_time
        return elapsed_time


class Profiler:
    """ Simple wrapper around cProfile """

    def __init__(self):
        self.profile = cProfile.Profile()

    def start(self):
        """ Starts profiling """
        self.profile.enable()

    def end(self, keys=None, restrictions=None):
        """ Stops profiling and prints a report """
        if keys is None:
            keys = ['cumulative']  # order by cumulative time

        if restrictions is None:
            restrictions = [20]  # top 20 lines only

        stats = pstats.Stats(self.profile)
        stats.sort_stats(*keys)
        stats.print_stats(*restrictions)
