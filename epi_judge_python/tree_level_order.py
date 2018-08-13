from test_framework import generic_test

from collections import deque, defaultdict

def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if not tree:
        return []

    level = 0
    q = deque([tree])
    result = []
    tmp = []
    countAtlevel = defaultdict(int)
    countAtlevel[0] = 1

    while q:
        node = q.popleft()
        tmp.append(node.data)

        if node.left:
            q.append(node.left)
            countAtlevel[level+1] += 1
        if node.right:
            q.append(node.right)
            countAtlevel[level+1] += 1

        countAtlevel[level] -= 1
        if countAtlevel[level] == 0:
            result.append(tmp.copy())
            tmp = []
            level += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
