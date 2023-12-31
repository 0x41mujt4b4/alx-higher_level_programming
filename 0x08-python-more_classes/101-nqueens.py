#!/usr/bin/python3

def can_place(board, row, col):
    for i in range(col):
        queen_can_attack = [
                board[i] == row,
                board[i] - i == row - col,
                board[i] + i == row + col
                ]
        if any(queen_can_attack):
            return False
    return True


def place_queens(board, col, n):
    if col == n:
        result.append(board[:])
        return
    for row in range(n):
        if can_place(board, row, col):
            board[col] = row
            place_queens(board, col + 1, n)
            board[col] = -1


if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    result = []
    board = [-1] * n
    place_queens(board, 0, n)
    for solution in result:
        print([[i, solution[i]] for i in range(len(solution))])
