"""
210_number_of_provinces

Question:
Count provinces (components) from adjacency matrix.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Approaches:
  1. DFS/BFS over unvisited cities  ->  O(n^2) time, O(n) space
  2. Union-Find over connected pairs  ->  O(n^2 * a) time, O(n) space
"""

# TODO: implement your solution here