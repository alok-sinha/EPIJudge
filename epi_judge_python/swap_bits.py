from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    y = x
    if (x >> i & 0x1) ^ ( x >> j & 0x1):
        y = x ^ (1 << i | 1 << j)

    return y


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
