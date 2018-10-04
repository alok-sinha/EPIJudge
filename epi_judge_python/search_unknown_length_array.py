from test_framework import generic_test


def binary_search_unknown_length(A, k):
    # TODO - you fill in here.

    l= 1

    while True:
        try:
            if A[l] == k:
                return l
            l *= 2
        except IndexError:
            break

    left, right = 0, l



    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_unknown_length_array.py",
                                       'search_unknown_length_array.tsv',
                                       binary_search_unknown_length))
