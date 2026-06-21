"""
191_number_of_islands

Question:
Count islands in a 2D grid.

Input: grid = [...]
Output: 1

Approaches:
  1. DFS marking visited cells in-place  ->  O(m*n) time, O(m*n) space (recursion stack)
  2. BFS with queue marking visited  ->  O(m*n) time, O(min(m,n)) space
  3. Union-Find connecting adjacent land  ->  O(m*n * a(m*n)) time, O(m*n) space
"""

# TODO: implement your solution here