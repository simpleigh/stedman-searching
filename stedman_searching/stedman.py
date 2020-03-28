from stedman_searching.rows import perm_from_row


""" Rows reachable at the end of a six-pair starting at rounds """
PAIR_END_ROWS = [
    '2468103E597',    # 1. pp
    '246810375E9',    # 2. p-
    '2468103759E',    # 3. ps
    '246819305E7',    # 4. -p
    '2468193750E',    # 5. --
    # '246819375E0',  # 6. -s (prefer s-)
    '2468193E507',    # 7. sp
    '246819375E0',    # 8. s-
    # '2468193750E',  # 9. ss (prefer --)
]


""" Permutations reachable at the end of a six-pair starting at rounds """
PAIR_END_PERMS = [perm_from_row(row) for row in PAIR_END_ROWS]


def multiply_end_perms_from_perm(perm):
    """
    Compute permutations reachable from an arbitrary permutation

    Given an arbitrary permutation, returns a list of all permutations reachable
    at the end of a six-pair starting from that permutation.

    This function uses `sympy` `Permutation` multiplication for computation.
    """
    return [
        quick_six_end_perm * perm  # n.b. ordering
        for quick_six_end_perm in PAIR_END_PERMS
    ]
