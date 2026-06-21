"""
062_game_of_life

Question:
Compute next Conway's Game of Life state in-place.

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: next state

Approaches:
  1. Copy board, compute from copy  ->  O(m*n) time, O(m*n) space
  2. Bit-encoded next state in same cell (use 2nd bit)  ->  O(m*n) time, O(1) space
"""

# TODO: implement your solution here