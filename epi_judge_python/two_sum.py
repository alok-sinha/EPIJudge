from test_framework import generic_test


def has_two_sum(A, t):
    # TODO - you fill in here.

    start, end = 0, len(A)-1
    while start < end:
        s = A[start] + A[end]
        if s == t:
            return True
        elif s > t:
            end -= 1
        else:
            start += 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
