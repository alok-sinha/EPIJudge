from test_framework import generic_test


def rotate_matrix(square_matrix):
    # TODO - you fill in here.

    if len(square_matrix) <= 1:
        return

    n = len(square_matrix)
    start, end = 0, n-1
    while n > 1:
        print("n = ", n)
        for i in range(start, end):
            x = square_matrix[i][end]
            square_matrix[i][end] = square_matrix[start][i]
            print(i,end)

            y = square_matrix[end][end-i]
            square_matrix[end][end-i-start] = x
            print(end,end-i-start)

            x = square_matrix[end-i][start]
            square_matrix[end-i-start][start] = y
            print(end-i-start,start)

            square_matrix[start][i] = x
            print(start,i)
        n -= 2
        start += 1
        end -= 1
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
