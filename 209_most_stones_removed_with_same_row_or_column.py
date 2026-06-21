"""
209_most_stones_removed_with_same_row_or_column

Question:
Max stones removable leaving one per connected row/col group.

Input: stones = [[0,0],[0,1],...]
Output: 5

Approaches:
  1. Union-Find on rows and columns (index rows, ~columns)  ->  O(n * a) time, O(n) space
  2. DFS on stone graph counting components  ->  O(n^2) time, O(n) space
  3. Answer = total stones - number of components  ->  O(n) time with DSU
"""

# TODO: implement your solution here