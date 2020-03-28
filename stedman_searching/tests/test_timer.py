import unittest

from stedman_searching.timer import Timer


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
