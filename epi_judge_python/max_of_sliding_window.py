import functools


from collections import deque

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume
    def __eq__ (self, o2):
        return self.volume == o2.volume
    def __gt__ (self, o2):
        return self.volume > o2.volume
    def __lt__ (self, o2):
        return self.volume < o2.volume


def calculate_traffic_volumes(A, w):
    # TODO - you fill in here.

    q = deque()
    qMax = deque()

    A.sort(key=lambda x : x.time)


    result = []

    count = 0
    for te in A:
        q.append(te)
        count += 1
        if qMax:
            if te.volume > qMax[-1].volume:
                qMax.append(te)
            else:
                qMax.append(qMax[-1])
        else:
            qMax.append(te)

        result.append(TrafficElement(te.time, qMax[-1].volume))

        if count == w:
            q.popleft()
            qMax.popleft()

    return result


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_of_sliding_window.py",
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
