import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
from collections import deque


def search_maze(maze, s, e):
    # TODO - you fill in here.

    def createPath():
        path = [e]
        child = e
        while parent[child]:
            path.insert(0, Coordinate(parent[child][0], parent[child][1]))
            child = parent[child]

        return path

    def getEdges(node):
        x,y = node
        d = [Coordinate(x + i, y) for i in [-1, 1] if x+i < l and x+i >= 0 and not maze[x + i][y]]
        d.extend(Coordinate(x, y + i) for i in [-1, 1] if y+i < b and y+i >= 0 and not maze[x][y + i])

        return d

    g = {}
    g[s] = "Discovered"

    l, b = len(maze), len(maze[0])
    parent = {(s[0], s[1]):None}

    q = deque([(s[0],s[1])])
    q.append(s)


    while q:
        node = q.popleft()
        for edge in getEdges(node):

            if edge == e:
                parent[e] = node
                return createPath()

            if edge not in g:
                q.append(edge)
                parent[edge] = node
                g[edge] = "Discovered"
        g[node] = "Processed"

    return []


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
