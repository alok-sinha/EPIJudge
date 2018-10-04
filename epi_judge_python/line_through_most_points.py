import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import defaultdict

Point = collections.namedtuple("Point", ("x", "y"))


def find_line_with_most_points(points):
    # TODO - you fill in here.


    def getLine(p1,p2):
        #
        # slope = y2-y1/x2-x1
        # c = y - mx

        if p1.x == p2.x:
            return float("inf"), p1.x
        elif p1.y == p2.y:
            return 0, p1.y
        else:
            m = (p1.y-p2.y)/(p1.x - p2.x)
            c = p2.y - m*p2.x
            return m,c

    lines = defaultdict(set)

    n = len(points)
    maxPoints = 0
    for i in range(n):
        for j in range(i+1, n):
            m,c = getLine(points[i], points[j])

            if lines[(m,c)]:
                if points[i] not in lines[(m,c)]:
                    lines[(m,c)].add(points[i])
            else:
                lines[(m,c)].add(points[i])

            if lines[(m,c)]:
                if points[j] not in lines[(m,c)]:
                    lines[(m,c)].add(points[j])
            else:
                lines[(m,c)].add(points[j])


            if len(lines[(m,c)]) > maxPoints:
                maxPoints = len(lines[(m,c)])
                print (m,c, ":",lines[(m,c)])

    return maxPoints


@enable_executor_hook
def find_line_with_most_points_wrapper(executor, points):
    points = [Point(*x) for x in points]
    return executor.run(functools.partial(find_line_with_most_points, points))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("line_through_most_points.py",
                                       'line_through_most_points.tsv',
                                       find_line_with_most_points_wrapper))
