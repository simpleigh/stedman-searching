from stedman_searching.rows import perm_from_row


QUICK_SIX_END_ROWS = [
    '2468103E597',  # pp
    '246810375E9',  # p-
    '2468103759E',  # ps
    '246819305E7',  # -p
    '2468193750E',  # --
    # '246819375E0',  # -s  prefer s-
    '2468193E507',  # sp
    '246819375E0',  # s-
    # '2468193750E',  # ss  prefer --
]


QUICK_SIX_END_PERMS = [perm_from_row(row) for row in QUICK_SIX_END_ROWS]


def generate_next_perms(perm):
    return [
        quick_six_end_perm * perm  # n.b. ordering
        for quick_six_end_perm in QUICK_SIX_END_PERMS
    ]
