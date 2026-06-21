"""
197_surrounded_regions

Question:
Flip 'O' regions not connected to border to 'X'.

Input: board = [...]
Output: surrounded flipped

Approaches:
  1. DFS/BFS from border 'O' cells marking safe  ->  O(m*n) time, O(m*n) space
  2. Union-Find connecting border 'O's to a virtual node  ->  O(m*n * a) time, O(m*n) space
"""

# TODO: implement your solution here