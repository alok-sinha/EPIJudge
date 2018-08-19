import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount, A):
    # TODO - you fill in here.
    def reverse(i,j):
        start, end = i,j
        while start < end and end < n:
            A[start],A[end] = A[end], A[start]
            start, end = start+1, end-1
    n = len(A)

    rotate_amount = rotate_amount % n
    reverse(0, n-rotate_amount-1)
    reverse(n-rotate_amount, n-1)
    reverse(0,n-1)

    return


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rotate_array.py", 'rotate_array.tsv',
                                       rotate_array_wrapper))
