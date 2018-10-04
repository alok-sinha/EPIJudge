import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    # TODO - you fill in here.

    def lookUpKey(tree):

        if not tree:
            return []

        if tree.data >= start and tree.data <= end:
            lookUpKey(tree.left)
            result.append(tree.data)
            lookUpKey(tree.right)
        elif tree.data < start:
            lookUpKey(tree.right)
        else:
            lookUpKey(tree.left)

    result = []
    start, end = interval[0], interval[1]
    lookUpKey(tree)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
