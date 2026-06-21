"""
195_rotting_oranges

Question:
Min time until all oranges rot (multi-source BFS).

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Approaches:
  1. Multi-source BFS from all rotten oranges  ->  O(m*n) time, O(m*n) space
  2. DFS from each rotten (suboptimal)  ->  O(m*n) time, O(m*n) space
"""

# TODO: implement your solution here