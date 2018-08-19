import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    # TODO - you fill in here.
    #cost[c][n] = max(cost[c-W(n)][n-1] + V(n), cost[c][n-1])

    cache = {}

    def findMaxCost(n, capacity):
        if capacity <= 0 or n < 0:
            return 0

        if (n,capacity) in cache:
            return cache[(n,capacity)]

        lastItem = items[n]
        o1 = 0
        if lastItem[0] <= capacity:
            o1 = findMaxCost(n-1, capacity-lastItem[0]) + lastItem[1]
        o2 = findMaxCost(n-1, capacity)

        cache[(n,capacity)] = max(o1, o2)
        return max(o1, o2)

    n = len(items)
    cache = [[0 for i in range(capacity+1)] for j in range(n+1)]

    for c in range(1,capacity+1):
       for j in range(1,n+1):
           item = items[j-1]
           if item[0] <= c:
              cache[j][c] = max(cache[j-1][c-item[0]] + item[1], cache[j-1][c])
           else:
              cache[j][c] = cache[j-1][c]


    #return findMaxCost(l-1, capacity)
    return cache[n][capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
