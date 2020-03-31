from stedman_searching.rows import perm_from_row


""" Rows reachable at the end of a six-pair starting at rounds """
PAIR_END_ROWS = {
    7: [
        '2467153',  # 1. pp
        '2463175',  # 2. p-
        '2463157',  # 3. ps
        '2456173',  # 4. -p
        '2453167',  # 5. --
        '2457163',  # 7. sp
        '2453176',  # 8. s-
    ],
    9: [
        '246819375',  # 1. pp
        '246815397',  # 2. p-
        '246815379',  # 3. ps
        '246718395',  # 4. -p
        '246715389',  # 5. --
        '246719385',  # 6. sp
        '246715398',  # 7. s-
    ],
    11: [
        '2468103E597',  # 1. pp
        '246810375E9',  # 2. p-
        '2468103759E',  # 3. ps
        '246819305E7',  # 4. -p
        '2468193750E',  # 5. --
        '2468193E507',  # 7. sp
        '246819375E0',  # 8. s-
    ],
}


""" Permutations reachable at the end of a six-pair starting at rounds """
PAIR_END_PERMS = {
    stage: [perm_from_row(row) for row in PAIR_END_ROWS[stage]]
    for stage in PAIR_END_ROWS
}


def multiply_end_perms_from_perm(perm):
    """
    Compute permutations reachable from an arbitrary permutation

    Given an arbitrary permutation, returns a list of all permutations reachable
    at the end of a six-pair starting from that permutation.

    This function uses `sympy` `Permutation` multiplication for computation.
    """
    return [
        quick_six_end_perm * perm  # n.b. ordering
        for quick_six_end_perm in PAIR_END_PERMS[perm.size]
    ]
