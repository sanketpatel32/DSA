"""
198_walls_and_gates

Question:
Fill each empty room with distance to nearest gate.

Input: rooms = [[inf,-1,0,inf],...]
Output: distance-filled

Approaches:
  1. Multi-source BFS from all gates  ->  O(m*n) time, O(m*n) space
  2. DFS from each gate (suboptimal)  ->  O(m*n) time, O(m*n) space
"""

# TODO: implement your solution here