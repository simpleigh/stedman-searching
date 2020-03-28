from math import factorial
import unittest

from stedman_searching.distances_table import DistancesTable


class DistancesTableTestCase(unittest.TestCase):

    def test_create(self):
        table = DistancesTable(1)
        self.assertIs(len(table), 1)

    def test_create_longer_distances(self):
        for stage in range(2, 8):
            with self.subTest(stage=stage):
                table = DistancesTable(stage)
                self.assertEqual(len(table), factorial(stage))

    def test_starts_empty(self):
        table = DistancesTable(4)
        for i in range(24):
            self.assertFalse(i in table)

    def test_starts_zero(self):
        table = DistancesTable(4)
        for distance in table:
            self.assertEqual(distance, 0)

    def test_can_add(self):
        table = DistancesTable(4)

        table.add(12, 6)

        self.assertTrue(12 in table)
        self.assertEqual(table[12], 6)

    def test_ignores_longer_distances(self):
        table = DistancesTable(4)
        table.add(12, 6)

        table.add(12, 8)

        self.assertEqual(table[12], 6)

    def test_allows_shorter_distances(self):
        table = DistancesTable(4)
        table.add(12, 6)

        table.add(12, 4)

        self.assertEqual(table[12], 4)

    def test_starts_with_empty_counts(self):
        table = DistancesTable(4)
        self.assertEqual(table.get_counts(), [24])

    def test_computes_counts_correctly(self):
        table = DistancesTable(4)
        table.add(0, 2)
        table.add(1, 4)
        table.add(2, 4)
        table.add(3, 4)
        table.add(4, 6)
        table.add(5, 6)
        table.add(6, 6)
        table.add(7, 6)
        table.add(8, 6)
        table.add(9, 6)

        self.assertEqual(table.get_counts(), [14, 1, 3, 6])

