from test_framework import generic_test

from collections import deque, defaultdict

def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if not tree:
        return []

    q = deque([tree])
    q2 = deque()
    result = [[tree.data]]

    while q or q2:
        node = q.popleft()

        if node.left:
            q2.append(node.left)
        if node.right:
            q2.append(node.right)

        if not q:
            tmp = []
            for i in range(len(q2)):
                tmp.append(q2[i].data)

            if tmp:
                result.append(tmp)
            q,q2 = q2,q

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
