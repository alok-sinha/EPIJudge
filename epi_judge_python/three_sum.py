from test_framework import generic_test

import two_sum
def has_three_sum(A, t):
    # TODO - you fill in here.
    A.sort()

    for i, num in enumerate(A):
        if two_sum.has_two_sum(A, t-num):
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
