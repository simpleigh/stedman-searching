"""
Functions to convert between different ways of expressing rows
"""

from sympy.combinatorics import Permutation


"""
Mapping of bell symbols to bell numbers

Ringers use the following symbols to describe bells: `1234567890ETABC`.
This map is a string translation table from these characters to a bell number.
"""
BELL_TRANSLATIONS = str.maketrans({
    '0': '10',
    'E': '11',
    'T': '12',
    'A': '13',
    'B': '14',
    'C': '15',
})


def perm_from_row(row):
    """ Converts a row string into a `sympy` `Permutation` """
    return Permutation([
        int(bell.translate(BELL_TRANSLATIONS)) - 1
        for bell in row
    ])


"""
Bell characters

The reverse of `BELL_TRANSLATIONS` described above.
"""
BELL_CHARACTERS = '1234567890ETABC'


def row_from_perm(perm):
    """ Converts a `sympy` `Permutation` into a row string """
    return ''.join([BELL_CHARACTERS[bell] for bell in perm])
