from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # TODO - you fill in here.

    def getHeight(node):

        if not node.left and not node.right:
            return 0

        lh, rh = 0,0
        if node.left:
            lh = 1 + getHeight(node.left)
        if node.right:
            rh = 1 + getHeight(node.right)
        return max(lh, rh)


    if not tree:
        return True

    if tree.left and tree.right:
        leftHeight = getHeight(tree.left)
        rightHeight = getHeight(tree.right)
        print("H:", leftHeight, rightHeight)

        return abs(leftHeight - rightHeight) <= 1
    elif tree.left:
        return getHeight(tree.left) == 0
    elif tree.right:
        return getHeight(tree.right) == 0

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
