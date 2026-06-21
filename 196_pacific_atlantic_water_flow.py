"""
196_pacific_atlantic_water_flow

Question:
Cells that can flow to both oceans (edges).

Input: heights = [...]
Output: list of cells

Approaches:
  1. DFS from each ocean inward, intersect reachability  ->  O(m*n) time, O(m*n) space
  2. BFS from both ocean borders  ->  O(m*n) time, O(m*n) space
"""

# TODO: implement your solution here