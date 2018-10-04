import copy

from test_framework import generic_test


def rook_attack(A):
    # TODO - you fill in here.

    def setAttacks(row, col):
        for i in range(0, m):
            if A[i][col] == 1:
                A[i][col] = 3
            elif A[i][col] == 0:
                A[i][col] = 2

        for j in range(0, n):
            if A[row][j] == 1:
                A[row][j] = 3
            elif A[row][j] == 0:
                A[row][j] = 2

    if not A:
        return

    m = len(A)
    n = len(A[0])

    for i in range(m):
        for j in range(n):
            if A[i][j] == 0 or A[i][j] == 2:
                setAttacks(i, j)

    for i in range(m):
        for j in range(n):
            if A[i][j] == 2 or A[i][j] == 3:
                A[i][j] = 0


    return


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rook_attack.py", 'rook_attack.tsv',
                                       rook_attack_wrapper))
