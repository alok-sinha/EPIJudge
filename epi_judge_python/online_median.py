from test_framework import generic_test

import heapq
def online_median(sequence):
    # TODO - you fill in here.
    print(type(sequence))

    n = len(list(sequence))
    if n == 0:
        return []
    elif n == 1:
        return sequence
    elif n == 2:
        return [(sequence[0]+ sequence[1])/2]

    left, right = sequence[0], sequence[1] if sequence[0] < sequence[1] else sequence[1], sequence[0]
    median = []


    for i in range(2,n):
        num = sequence[i]
        nLeft, nRight = len(left), len(right)
        if not nLeft:
            left[0] = -num
            continue

        if num <= -left[0]:#Belongs to  left heap
            if nLeft == nRight:
                heapq.heappush(left, -num)
            else:
                x = heapq.heappushpop(left, -num)
                heapq.heappush(-x)
        else: #Should go to right
            if nLeft == nRight:
                x = heapq.heappushpop(right,num)
                heapq.heappush(left,-x)
            else:
                heapq.heappush(right, num)

        if len(left)  == len(right):
            median.append((-left[0] + right[0])/2)
        else:
            median.append(-left[0])


    return median


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
