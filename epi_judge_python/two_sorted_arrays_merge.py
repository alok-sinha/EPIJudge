from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    # TODO - you fill in here.

    i,j = m-1, n-1
    w = len(A)-1

    while i > -1 and j > -1:
        if A[i] > B[j]:
            A[w] = A[i]
            i -= 1
        else:
            A[w] = B[j]
            j -= 1
        w -= 1

    while j > -1:
        A[w] = B[j]
        w, j = w-1, j-1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
