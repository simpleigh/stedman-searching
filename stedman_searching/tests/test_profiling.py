import unittest
from unittest.mock import patch

from stedman_searching.profiling import Profiler, Timer


class TimerTestCase(unittest.TestCase):

    def test_can_be_created(self):
        Timer()
        # succeeds if no errors

    def test_returns_nonzero_split(self):
        timer = Timer()
        self.assertGreater(timer.split(), 0)

    def test_splits_not_always_increasing(self):
        timer = Timer()
        splits = [timer.split() for _ in range(10)]
        self.assertNotEqual(splits, list(sorted(splits)))


class ProfilerTestCase(unittest.TestCase):

    def test_can_be_created(self):
        Profiler()
        # succeeds if no errors

    @patch('cProfile.Profile')
    def test_starts_profiling(self, Profile):
        profiler = Profiler()

        Profile.return_value.enable.assert_not_called()

        profiler.start()

        Profile.return_value.enable.assert_called_once()


    @patch('cProfile.Profile')
    @patch('pstats.Stats')
    def test_stops_profiling(self, Stats, cProfile):
        profiler = Profiler()
        stats = Stats.return_value

        profiler.end()

        Stats.assert_called_once_with(cProfile.return_value)
        stats.sort_stats.assert_called_once_with('cumulative')
        stats.print_stats.assert_called_once_with(20)

    @patch('pstats.Stats')
    def test_allows_stats_to_be_customised(self, Stats):
        profiler = Profiler()
        stats = Stats.return_value

        profiler.end(keys=['time', 'cumulative'], restrictions=[10, 'init'])

        stats.sort_stats.assert_called_once_with('time', 'cumulative')
        stats.print_stats.assert_called_once_with(10, 'init')
