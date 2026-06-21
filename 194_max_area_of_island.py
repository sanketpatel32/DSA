"""
194_max_area_of_island

Question:
Max area of an island in a grid.

Input: grid = [...]
Output: 6

Approaches:
  1. DFS counting connected land  ->  O(m*n) time, O(m*n) stack
  2. BFS counting connected land  ->  O(m*n) time, O(m*n) space
  3. Union-Find tracking component sizes  ->  O(m*n * a(m*n)) time, O(m*n) space
"""

# TODO: implement your solution here