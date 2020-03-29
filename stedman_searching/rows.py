"""
Ways of expressing rows and functions to convnert between those ways
"""

from sympy.combinatorics import Permutation


def perm_for_rounds(stage):
    """ Rounds on a particular number of bells """
    return Permutation(stage - 1)


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


class SetRow:
    """
    A container for a row within a set

    Attaches additional metadata to the row without affecting its storage in
    a Python `set`. Comparison and hash operations ignore the metadata and only
    consider the row itself.
    """

    def __init__(self, row, **metadata):
        self.row = row
        self.metadata = metadata

    def __eq__(self, other):
        """ Compare rows directly ignoring metadata """
        return self.row == other.row

    def __getattr__(self, name):
        """ Allow metadata to be accessed as attributes """
        try:
            return self.metadata[name]
        except KeyError as error:
            raise AttributeError() from error

    def __hash__(self):
        """ Hash the row ignoring metadata """
        return hash(self.row)

    def __repr__(self):
        params = [f"'{self.row}'"]
        params = params + [
            f'{key}={repr(value)}'
            for key, value in self.metadata.items()
        ]
        params = ', '.join(params)

        return f"SetRow({params})"

    def __str__(self):
        return self.row
