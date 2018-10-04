from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    # TODO - you fill in here.
    b = [[0 for j in range(k+1) ] for i in range(n+1)]

    for j in range(0,k+1):
        b[0][j] = 0

    for i in range(0, n+1):
        b[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            b[i][j] = b[i-1][j]+ b[i-1][j-1]

    return b[n][k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
