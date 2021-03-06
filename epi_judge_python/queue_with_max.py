from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque


class QueueWithMax:
    def __init__(self):
        self.queue = deque()
        self.maxQueue = deque()

    def enqueue(self, x):
        # TODO - you fill in here.

        self.queue.append(x)
        self.maxQueue.append(x)

        for i in range(len(self.maxQueue)-2, -1, -1):
            if x > self.maxQueue[i]:
                self.maxQueue[i] = x
            else:
                break
        return

    def dequeue(self):
        # TODO - you fill in here.
        self.maxQueue.popleft()

        return self.queue.popleft()

    def max(self):
        # TODO - you fill in here.
        return self.maxQueue[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
