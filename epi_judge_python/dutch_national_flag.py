import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):

    last = len(A)-1
    equal, larger = last, last + 1
    pivot = A[pivot_index]
    A[pivot_index], A[equal] = A[equal], A[pivot_index]

    j = 0
    while j < equal:
        if A[j] > A[equal]:

            A[j], A[equal - 1] = A[equal - 1], A[j]
            A[equal - 1], A[larger - 1] = A[larger - 1], A[equal - 1]

            equal -= 1
            larger -= 1

        elif A[j] == A[equal]:
            A[j], A[equal - 1] = A[equal - 1], A[j]
            equal -= 1

        else:
            j += 1
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
