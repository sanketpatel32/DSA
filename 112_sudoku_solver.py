"""
112_sudoku_solver

Question:
Solve a 9x9 Sudoku in-place.

Input: board = [...]
Output: solved board

Approaches:
  1. Backtracking trying 1-9 in empty cells with validity checks  ->  O(9^(n*n)) time, O(n*n) space
  2. Backtracking with constraint sets per row/col/box  ->  O(9^(n*n)) time (faster constants)
"""

# TODO: implement your solution here