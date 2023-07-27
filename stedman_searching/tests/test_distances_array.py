from math import factorial

import pytest

from stedman_searching.distances_array import DistancesArray


class TestDistancesArray:
    def test_create(self):
        array = DistancesArray(1)
        assert len(array) == 1

    @pytest.mark.parametrize('stage', range(2, 8))
    def test_create_longer_distances(self, stage):
        array = DistancesArray(stage)
        assert len(array) == factorial(stage)

    def test_starts_empty(self):
        array = DistancesArray(4)
        for i in range(24):
            assert i not in array

    def test_starts_zero(self):
        array = DistancesArray(4)
        for distance in array:
            assert distance == 0

    def test_can_add(self):
        array = DistancesArray(4)

        array.add(12, 6)

        assert 12 in array
        assert array[12] == 6

    def test_ignores_new_distances(self):
        array = DistancesArray(4)
        array.add(12, 6)

        array.add(12, 8)

        assert array[12] == 6

    def test_starts_with_empty_counts(self):
        array = DistancesArray(4)
        assert array.get_counts() == [24]

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

        assert array.get_counts() == [14, 1, 3, 6]
