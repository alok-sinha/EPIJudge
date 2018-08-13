from test_framework import generic_test

from heapq import *

def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    h = []
    result = []

    for i, array in enumerate(sorted_arrays):
        heappush(h, (array.pop(0), i))

    while h:
        item, index = heappop(h)
        result.append(item)

        if sorted_arrays[index]:
            heappush(h, (sorted_arrays[index].pop(0), index))


    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
