from math import factorial

import numpy as np


class DistancesTable:
    """
    A table with space to store distances from rounds for n! rows

    Wraps a `numpy` array.
    """

    def __init__(self, stage):
        self._table = np.zeros(factorial(stage), np.int8)

    def __contains__(self, index):
        return self._table[index] > 0

    def __getitem__(self, index):
        return self._table[index]

    def __iter__(self):
        return iter(self._table)

    def __len__(self):
        return len(self._table)

    def add(self, index, distance):
        """
        Adds a new result to the table

        If the table already has an entry for a particular index then we check
        whether our new result is smaller before overwriting it.

        :return: whether the entry was added (for tree pruning)
        """

        if self._table[index] == 0 or self._table[index] > distance:
            self._table[index] = distance
            return True

        return False

    def get_counts(self):
        """
        Returns a histogram of distances

        This will be a single array containing the number of entries for each
        distance in order 0, 2, 4, 6, etc.
        """
        return [
            distance
            for distance in np.bincount(self._table)
            if distance > 0
        ]
