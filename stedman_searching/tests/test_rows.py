import unittest

from sympy.combinatorics import Permutation

from stedman_searching.rows import perm_from_row, row_from_perm


class RowsTestCase(unittest.TestCase):

    def test_perm_from_rounds(self):
        rounds = Permutation(range(11))
        self.assertEqual(
            perm_from_row('1234567890E'),
            rounds,
        )

    def test_row_from_rounds(self):
        rounds = Permutation(range(11))
        self.assertEqual(
            row_from_perm(rounds),
            '1234567890E',
        )

    def test_perm_from_reverse_rounds(self):
        reverse_rounds = Permutation(list(reversed(range(11))))
        self.assertEqual(
            perm_from_row('E0987654321'),
            reverse_rounds,
        )

    def test_row_from_reverse_rounds(self):
        reverse_rounds = Permutation(list(reversed(range(11))))
        self.assertEqual(
            row_from_perm(reverse_rounds),
            'E0987654321',
        )
