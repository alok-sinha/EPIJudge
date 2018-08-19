import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    # TODO - you fill in here.
    if node0 == node1:
        return node0


    def inorder(root, node0, node1, found):
        oneTrue = found[0] or found[1]

        if root == node0:
            found[0] = True
        elif root == node1:
            found[1] = True

        if found[0] and found[1]:
            return None

        if root.left:
            lcaroot = inorder(root.left, node0, node1, found)
            if lcaroot:
                return lcaroot

        if not (found[0] and found[1]) and root.right:
            lcaroot = inorder(root.right, node0, node1, found)
            if lcaroot:
                return lcaroot

        if not oneTrue and found[0] and found[1]:
            return root
        else:
            return None

    return inorder(tree, node0, node1, [False, False])


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
