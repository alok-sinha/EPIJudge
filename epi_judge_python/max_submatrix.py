from test_framework import generic_test


def max_rectangle_submatrix(A):
    # TODO - you fill in here.

    def countMaxCont(x):
        print(x)
        maxC = 0
        count = 0
        for i in x:
            if i:
                count += 1
            else:
                maxC = max(maxC, count)
                count = 0

        maxC = max(maxC, count)
        print(maxC)
        return maxC

    if not A:
        return 0

    m, n = len(A), len(A[0])

    x = [A[0][j] for j in range(n)]
    maxArea = countMaxCont(x)
    for i in range(1, m):
        x = [x[j] and A[i][j] for j in range(n)]
        maxArea = max(maxArea, countMaxCont(x)*(i + 1))

    return maxArea


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_submatrix.py", 'max_submatrix.tsv',
                                       max_rectangle_submatrix))
