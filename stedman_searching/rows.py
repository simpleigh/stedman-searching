from sympy.combinatorics import Permutation


BELL_TRANSLATIONS = str.maketrans({ '0': '10', 'E': '11' })


def perm_from_row(row):
    return Permutation([
        int(bell.translate(BELL_TRANSLATIONS)) - 1
        for bell in row
    ])


BELL_CHARACTERS = '1234567890E'


def row_from_perm(perm):
    return ''.join([BELL_CHARACTERS[bell] for bell in perm])
