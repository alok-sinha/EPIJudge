from test_framework import generic_test

import heapq

def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.

    h = []
    for i in range(k):
        heapq.heappush(h, (sequence[i],i))

    for i in range(k, len(sequence)):
        item, index = heapq.heappop(h)
        sequence[index], sequence[i-k] = sequence[index], sequence[i-k]

        heapq.heappush(h, (sequence[i], i))

    return sequence


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
