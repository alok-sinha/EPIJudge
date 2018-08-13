from test_framework import generic_test


def is_symmetric(tree):
    # TODO - you fill in here.
    print(type(tree))

    def checkSymmetry(left, right):

        if (left != None) ^ (right != None):
            return False

        if not left and not right:
            return True

        if left.data != right.data:
            return False

        if checkSymmetry(left.left, right.right ) == False:
            return False

        return checkSymmetry(left.right, right.left)

    if not tree:
         return True

    return checkSymmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
