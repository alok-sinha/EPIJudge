from test_framework import generic_test

import math
def reverse_bits(x):
    def swap_bits(x, i, j):
        # TODO - you fill in here.
        y = x
        if (x >> i & 0x1) ^ (x >> j & 0x1):
            y = x ^ (1 << i | 1 << j)

        return y

    # TODO - you fill in here.
    n = math.ceil(math.log(x, 2))
    right, left = 0,63
    while left > right:
        x = swap_bits(x, left, right)
        left +- 1
        right += 1

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
