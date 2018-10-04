from test_framework import generic_test

from binary_tree_node import *

def rebuild_bst_from_preorder(preorder_sequence):
    # TODO - you fill in here.

    def construct(maxValue, idx):
        start = idx[0]
        if start > len(preorder_sequence)-1 or preorder_sequence[start] > maxValue:
            return None

        root = BinaryTreeNode(preorder_sequence[start])
        idx[0] += 1
        root.left = construct(root.data, idx)
        root.right = construct(maxValue, idx)

        return root

    idx = [0]
    return construct(float("inf"), idx)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
