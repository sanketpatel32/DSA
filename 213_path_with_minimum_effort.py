"""
213_path_with_minimum_effort

Question:
Min effort path (max edge diff along path) top-left to bottom-right.

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2

Approaches:
  1. Dijkstra variant on (effort,node)  ->  O(m*n log(m*n)) time, O(m*n) space
  2. Binary search + BFS/DFS feasibility  ->  O(m*n log max) time, O(m*n) space
  3. Union-Find sorting edges by effort until connected  ->  O(m*n log(m*n)) time, O(m*n) space
"""

# TODO: implement your solution here