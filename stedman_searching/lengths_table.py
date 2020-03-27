from math import factorial

import numpy as np


class LengthsTable:
    def __init__(self, bells):
        self._table = np.zeros(factorial(bells), np.int8)

    def __contains__(self, index):
        return self._table[index] > 0

    def __getitem__(self, index):
        return self._table[index]

    def __iter__(self):
        return iter(self._table)

    def __len__(self):
        return len(self._table)

    def add(self, index, distance):
        if self._table[index] == 0 or self._table[index] > distance:
            self._table[index] = distance
            return True

        return False
