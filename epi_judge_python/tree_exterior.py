import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def exterior_binary_tree(tree):
    # TODO - you fill in here.
    edges = []

    def inorderWalk(node, readLeft):

        if not node:
            return

        if not node.left and not node.right:
            edges.append(node)
            readLeft["read"] = False
            return

        if readLeft["read"]:
            edges.append(node)

        if node.left:
            inorderWalk(node.left, readLeft)
        if node.right:
            inorderWalk(node.right, readLeft)

    if not tree:
        return []

    edges = [tree]
    inorderWalk(tree.left, {"read":1})
    inorderWalk(tree.right, {"read":0})


    stack = []
    right = tree.right
    while right and (right.right or right.left):
        stack.append(right)
        if right.right:
            right = right.right
        else:
            right = right.left

    while stack:
        edges.append(stack.pop())

    return edges


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
