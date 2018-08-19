import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def create_list_of_leaves(tree):
    # TODO - you fill in here.

    def inorder(root, leaves):

        if not root:
            return

        if not root.left and not root.right:
            leaves.append(root)
            return

        inorder(root.left, leaves)
        inorder(root.right, leaves)


    leaves = []
    inorder(tree, leaves)


    return leaves


@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure("Result list can't contain None")
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_connect_leaves.py",
                                       "tree_connect_leaves.tsv",
                                       create_list_of_leaves_wrapper))
