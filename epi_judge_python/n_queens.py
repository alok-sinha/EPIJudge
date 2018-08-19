from test_framework import generic_test


def n_queens(n):
    # TODO - you fill in here.

    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []

    def canPlace(row, col):
        if board[row].count(1) != 0:
            return False
        if [board[i][col] for i in range(n)].count(1) != 0:
            return False

        up, down, j = row-1, row+1, col+1
        while j < n:
            if up >= 0 and board[up][j]:
                return False
            up -= 1

            if down < n and board[down][j]:
                return False
            down += 1

            j += 1

        up, down, j = row-1, row+1, col-1
        while j >= 0:
            if up >= 0 and board[up][j]:
                return False
            up -= 1

            if down < n and board[down][j]:
                return False
            down += 1

            j -= 1

        return True

    def placeQueen(row):
        if row == n:
            result.append(list(current))
            return

        for col in range(n):
            if canPlace(row,col):
                board[row][col] = 1
                current.append(col)

                placeQueen(row+1)

                board[row][col] = 0
                current.pop()

    current = []
    placeQueen(0)

    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
