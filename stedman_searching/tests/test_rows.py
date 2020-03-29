import unittest

from sympy.combinatorics import Permutation

from stedman_searching.rows import (
    perm_for_rounds,
    perm_from_row,
    row_from_perm,
    SetRow,
)


class RowsTestCase(unittest.TestCase):

    def test_perm_for_rounds_perm(self):
        for stage in range(7, 17, 2):
            with self.subTest(stage=stage):
                self.assertEqual(
                    perm_for_rounds(stage),
                    Permutation(stage - 1),
                )

    def test_perm_for_rounds_row(self):
        for stage in range(7, 17, 2):
            with self.subTest(stage=stage):
                self.assertEqual(
                    row_from_perm(perm_for_rounds(stage)),
                    '1234567890ETABC'[:stage],
                )

    def test_perm_from_row_rounds(self):
        rounds = Permutation(range(11))
        self.assertEqual(
            perm_from_row('1234567890E'),
            rounds,
        )

    def test_row_from_perm_rounds(self):
        rounds = Permutation(range(11))
        self.assertEqual(
            row_from_perm(rounds),
            '1234567890E',
        )

    def test_perm_from_row_reverse_rounds(self):
        reverse_rounds = Permutation(list(reversed(range(11))))
        self.assertEqual(
            perm_from_row('E0987654321'),
            reverse_rounds,
        )

    def test_row_from_perm_reverse_rounds(self):
        reverse_rounds = Permutation(list(reversed(range(11))))
        self.assertEqual(
            row_from_perm(reverse_rounds),
            'E0987654321',
        )


class SetRowTestCase(unittest.TestCase):

    def test_equal(self):
        row1 = SetRow('123')
        row2 = SetRow('123')
        self.assertEqual(row1, row2)

    def test_not_equal(self):
        row1 = SetRow('123')
        row2 = SetRow('213')
        self.assertNotEqual(row1, row2)

    def test_equal_despite_metadata(self):
        row1 = SetRow('123', key='value')
        row2 = SetRow('123', other=42)
        self.assertEqual(row1, row2)

    def test_exposes_metadata_as_attributes(self):
        row = SetRow('123', key='value', other=42)
        self.assertEqual(row.key, 'value')
        self.assertIs(row.other, 42)

    def test_raises_if_metadata_not_available(self):
        row = SetRow('123')
        with self.assertRaises(AttributeError):
            row.unknown

    def test_hashes_to_row(self):
        row = SetRow('123')
        self.assertEqual(hash(row), hash('123'))

    def test_hash_ignores_metadata(self):
        row = SetRow('123', key='value')
        self.assertEqual(hash(row), hash('123'))

    def test_set_ignores_metadata(self):
        row1 = SetRow('123', key='value')
        row2 = SetRow('123', other=42)
        self.assertIs(1, len(set([row1, row2])))

    def test_repr_no_metadata(self):
        row = SetRow('123')
        self.assertEqual(repr(row), "SetRow('123')")

    def test_repr_with_metadata(self):
        row = SetRow('123', key='value', other=42)
        self.assertEqual(repr(row), "SetRow('123', key='value', other=42)")

    def test_str_is_row(self):
        row = SetRow('123', key='value', other=42)
        self.assertEqual(str(row), '123')
