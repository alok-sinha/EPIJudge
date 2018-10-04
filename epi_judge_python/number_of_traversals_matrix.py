from test_framework import generic_test


def number_of_ways(n, m):
    # TODO - you fill in here.

    matrix = [[0 for i in range(m)] for i in range(n)]

    for i in range(n):
        matrix[i][m-1] = 1
    for j in range(m):
            matrix[n-1][j] = 1

    for col in range(m-2, -1,-1):
        for row in range(n-2, -1, -1):
            matrix[row][col] = matrix[row+1][col] + matrix[row][col+1]


    return matrix[0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
