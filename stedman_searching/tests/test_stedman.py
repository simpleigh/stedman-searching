import unittest

from stedman_searching.rows import perm_from_row, row_from_perm
from stedman_searching.stedman import multiply_end_perms_from_perm


class StedmanTestCase(unittest.TestCase):

    def test_rows_from_rounds(self):
        rounds = perm_from_row('1234567890E')
        perms = multiply_end_perms_from_perm(rounds)
        rows = [row_from_perm(perm) for perm in perms]
        self.assertEqual(rows, [
            '2468103E597',
            '246810375E9',
            '2468103759E',
            '246819305E7',
            '2468193750E',
            '2468193E507',
            '246819375E0',
        ])

    def test_rows_from_other_row(self):
        other = perm_from_row('527391E4068')
        perms = multiply_end_perms_from_perm(other)
        rows = [row_from_perm(perm) for perm in perms]
        self.assertEqual(rows, [
            '2314567890E',
            '2314567E980',
            '2314567E908',
            '2314507698E',
            '2314507E968',
            '2314507896E',
            '2314507E986',
        ])
