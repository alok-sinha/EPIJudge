from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.

    i = len(A)-1
    while i >= 0:

        A[i] = A[i] + 1
        carry = 0
        if A[i] == 10:
            A[i] = 0
            carry = 1

        if not carry:
            break
        i -= 1

    if carry:
        A.insert(0, 1)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
