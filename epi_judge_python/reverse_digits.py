from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.
    #Alok

    rev = 0
    xa = abs(x)
    while xa:
        digit = xa%10
        xa = xa //10
        rev = rev *10 + digit

    return rev if x > 0 else -rev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
