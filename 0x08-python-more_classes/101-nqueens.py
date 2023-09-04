#!/usr/bin/python3
"""N Queens Problem"""

import sys

def isSafe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, n, res):
    """Use backtracking to solve N Queen problem"""

    if col >= n:
        res.append([''.join(['Q' if x else '.' for x in row]) for row in board])
        return

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            solveNQUtil(board, col + 1, n, res)
            board[i][col] = 0

def printSolution(board, n):
    """Print one of the solutions"""
    res = []
    solveNQUtil(board, 0, n, res)
    for sol in res:
        new_sol = [[i, sol[i].index('Q')] for i in range(n)]
        print(new_sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialization of board
    board = [[0 for j in range(n)] for i in range(n)]

    # Solve and print solutions
    printSolution(board, n)

