from test_framework import generic_test


def levenshtein_distance(A, B):
    # TODO - you fill in here.

    #
    # dist(m,n) =  min(dist(m-1,n-1) if A[m] == B[n]
    #              min(dist(m-1,n) + 1, dist(m, n-1) + 1, dist(m-1, n-1) + 1)
    #

    M,N = len(A), len(B)
    dist = [[0 for n in range(N+1)] for m in range(M+1)]
    for m in range(0, M+1):
        dist[m][0] = m
    for n in range(0, N+1):
        dist[0][n] = n

    for m in range(1, M+1):
        for n in range(1, N+1):
            if A[m-1] == B[n-1]:
                dist[m][n] = dist[m-1][n-1]
            else:
                dist[m][n] = min(dist[m-1][n], dist[m][n-1], dist[m-1][n-1]) + 1

    return dist[M][N]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
