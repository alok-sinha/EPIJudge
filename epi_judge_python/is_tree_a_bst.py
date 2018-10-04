from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    print(tree)
    if not tree:
        return True

    if tree.left and tree.left.data >= tree.data:
        return False
    if tree.right and tree.right.data < tree.data:
        return False

    r = is_binary_tree_bst(tree.left)
    if r:
        r = is_binary_tree_bst(tree.right)

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
