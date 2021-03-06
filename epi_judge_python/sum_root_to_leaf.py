from test_framework import generic_test


def sum_root_to_leaf(tree, partial_path_sum=0):
    # TODO - you fill in here.

    if not tree:
        return 0

    partial_path_sum = partial_path_sum + tree.data
    if (tree.left == None) and (tree.right == None):
        return partial_path_sum

    return sum_root_to_leaf(tree.left, 2*partial_path_sum) + sum_root_to_leaf(tree.right, 2*partial_path_sum)





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
