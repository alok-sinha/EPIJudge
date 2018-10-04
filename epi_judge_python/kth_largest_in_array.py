from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
import random
def find_kth_largest(k, A):
    # TODO - you fill in here.


    def parition(left, right):
        pi = random.randint(left, right)
        piVal = A[pi]
        A[right], A[pi] = A[pi], A[right]

        i, newPivot = left, left
        while i < right:
            if A[i] > piVal:
                A[newPivot], A[i] = A[i], A[newPivot]
                newPivot += 1
            i += 1

        A[right], A[newPivot] = A[newPivot], A[right]
        return newPivot

    left,right = 0, len(A)-1
    while left <= right:
        p = parition(left, right)
        if p == (k-1):
            return A[p]
        elif p > (k-1):
            right = p - 1
        else:
            left = p + 1

    raise IndexError('no k-th node in array A')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
