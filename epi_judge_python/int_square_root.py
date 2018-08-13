from test_framework import generic_test


def square_root(k):
    # TODO - you fill in here.
    left, right = 0, k

    while left <= right:
        mid = (left + right)//2
        sq = mid*mid
        if sq > k:
            right = mid-1
        elif sq < k:
            left = mid+1
        else:
            return mid

    return left-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
