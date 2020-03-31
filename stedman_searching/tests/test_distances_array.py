from math import factorial
import unittest

from stedman_searching.distances_array import DistancesArray


class DistancesArrayTestCase(unittest.TestCase):

    def test_create(self):
        array = DistancesArray(1)
        self.assertIs(len(array), 1)

    def test_create_longer_distances(self):
        for stage in range(2, 8):
            with self.subTest(stage=stage):
                array = DistancesArray(stage)
                self.assertEqual(len(array), factorial(stage))

    def test_starts_empty(self):
        array = DistancesArray(4)
        for i in range(24):
            self.assertFalse(i in array)

    def test_starts_zero(self):
        array = DistancesArray(4)
        for distance in array:
            self.assertEqual(distance, 0)

    def test_can_add(self):
        array = DistancesArray(4)

        array.add(12, 6)

        self.assertTrue(12 in array)
        self.assertEqual(array[12], 6)

    def test_ignores_new_distances(self):
        array = DistancesArray(4)
        array.add(12, 6)

        array.add(12, 8)

        self.assertEqual(array[12], 6)

    def test_starts_with_empty_counts(self):
        array = DistancesArray(4)
        self.assertEqual(array.get_counts(), [24])

    def test_computes_counts_correctly(self):
        array = DistancesArray(4)
        array.add(0, 2)
        array.add(1, 4)
        array.add(2, 4)
        array.add(3, 4)
        array.add(4, 6)
        array.add(5, 6)
        array.add(6, 6)
        array.add(7, 6)
        array.add(8, 6)
        array.add(9, 6)

        self.assertEqual(array.get_counts(), [14, 1, 3, 6])

