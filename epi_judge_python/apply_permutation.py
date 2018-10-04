from test_framework import generic_test


def apply_permutation(perm, A):
    # TODO - you fill in here.
    # Alok


    #0,1,2,3,4
    #3,1,2,4,0

    #
    i = 0
    count = n = len(A)
    tmp = A[0]
    while count:
        while perm[i] == -1:
            i = (i + 1) % n

        dest = perm[i]
        perm[i] = -1
        A[dest],tmp = tmp, A[dest]
        count -= 1
    return A

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
