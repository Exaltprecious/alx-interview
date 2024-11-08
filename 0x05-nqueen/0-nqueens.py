#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def print_solution(board):
    """Print a valid solution."""

    print(board)

def is_safe(row, col, board, n):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        # Check column and diagonals
        if board[r] == col or \
           board[r] - r == col - row or \
           board[r] + r == col + row:
            return False
        return True

def solve_nqueens(row, board, n):
    """Backtrack to solve the N queens problem."""
    if row == n:  # All queens are placed
        print_solution(board)
        return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row] = col  # Place queen
            solve_nqueens(row + 1, board, n)  # Recur for the next row
            board[row] = -1  # Backtrack

def main():
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

    # Initialize the board
    board = [-1] * n
    solve_nqueens(0, board, n)

if __name__ == "__main__":
    main()=
