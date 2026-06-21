"""
031_valid_sudoku

Question:
Determine if a 9x9 Sudoku board is valid.

Input: board = [...]
Output: True

Approaches:
  1. Three passes: rows, columns, boxes with sets  ->  O(1) (81 cells) time, O(1) space
  2. Single pass with encoded (row/col/box,value) set keys  ->  O(1) time, O(1) space
"""

# TODO: implement your solution here