from test_framework import generic_test

from heapq import *
def online_median(sequence):
    # TODO - you fill in here.
    print(type(sequence))

    left, right = [],[]
    median = []

    for num in sequence:

        heappush(right, -heappushpop(left, -num))
        if len(left) < len(right):
            heappush(left, -heappop(right))

        if len(left) == len(right):
            median.append((-left[0] + right[0])/2)
        else:
            median.append(-left[0])

    return median








    return 0


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
