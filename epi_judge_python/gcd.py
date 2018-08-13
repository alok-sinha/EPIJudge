from test_framework import generic_test


def gcd(x, y):
    # TODO - you fill in here.

    while x > 1 and y > 1:
        if x > y:
            x = x%y
        else:
            y = y%x

    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
