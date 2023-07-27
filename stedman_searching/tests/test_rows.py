import pytest
from sympy.combinatorics import Permutation

from stedman_searching.rows import (
    perm_for_rounds,
    perm_from_row,
    row_from_perm,
    SetRow,
)


class TestRows:
    @pytest.mark.parametrize('stage', range(7, 17, 2))
    def test_perm_for_rounds_perm(self, stage):
        assert perm_for_rounds(stage) == Permutation(stage - 1)

    @pytest.mark.parametrize('stage', range(7, 17, 2))
    def test_perm_for_rounds_row(self, stage):
        assert row_from_perm(perm_for_rounds(stage)) == \
            '1234567890ETABC'[:stage]

    def test_perm_from_row_rounds(self):
        rounds = Permutation(range(11))
        assert perm_from_row('1234567890E') == rounds

    def test_row_from_perm_rounds(self):
        rounds = Permutation(range(11))
        assert row_from_perm(rounds) == '1234567890E'

    def test_perm_from_row_reverse_rounds(self):
        reverse_rounds = Permutation(list(reversed(range(11))))
        assert perm_from_row('E0987654321') == reverse_rounds

    def test_row_from_perm_reverse_rounds(self):
        reverse_rounds = Permutation(list(reversed(range(11))))
        assert row_from_perm(reverse_rounds) == 'E0987654321'


class TestSetRow:
    def test_equal(self):
        row1 = SetRow('123')
        row2 = SetRow('123')
        assert row1 == row2

    def test_not_equal(self):
        row1 = SetRow('123')
        row2 = SetRow('213')
        assert row1 != row2

    def test_equal_despite_metadata(self):
        row1 = SetRow('123', key='value')
        row2 = SetRow('123', other=42)
        assert row1 == row2

    def test_exposes_metadata_as_attributes(self):
        row = SetRow('123', key='value', other=42)
        assert row.key == 'value'
        assert row.other == 42

    def test_raises_if_metadata_not_available(self):
        row = SetRow('123')
        with pytest.raises(AttributeError):
            row.unknown

    def test_hashes_to_row(self):
        row = SetRow('123')
        assert hash(row) == hash('123')

    def test_hash_ignores_metadata(self):
        row = SetRow('123', key='value')
        assert hash(row) == hash('123')

    def test_set_ignores_metadata(self):
        row1 = SetRow('123', key='value')
        row2 = SetRow('123', other=42)
        assert len(set([row1, row2])) == 1

    def test_repr_no_metadata(self):
        row = SetRow('123')
        assert repr(row) == "SetRow('123')"

    def test_repr_with_metadata(self):
        row = SetRow('123', key='value', other=42)
        assert repr(row) == "SetRow('123', key='value', other=42)"

    def test_str_is_row(self):
        row = SetRow('123', key='value', other=42)
        assert str(row) == '123'
