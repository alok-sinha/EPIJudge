from test_framework import generic_test


def find_biggest_n_minus_one_product(A):
    # TODO - you fill in here.

    n = len(A)
    forward = [1 for i in range(n)]
    for i in range(1, n):
        forward[i] = A[i-1]*forward[i-1]

    backward = [1 for i in range(n)]
    for i in range(n-2, -1, -1):
        backward[i] = A[i+1]*backward[i+1]

    maxproduct = float("-inf")

    for i in range(n):
        maxproduct = max(maxproduct, forward[i]*backward[i])

    return maxproduct


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_product_all_but_one.py",
                                       'max_product_all_but_one.tsv',
                                       find_biggest_n_minus_one_product))
