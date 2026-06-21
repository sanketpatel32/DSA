"""
216_floyd_warshall_algorithm

Question:
All-pairs shortest paths (handles negative weights).

Input: weighted adjacency matrix
Output: distance matrix

Approaches:
  1. Triple loop over intermediate vertex k  ->  O(V^3) time, O(V^2) space
  2. With path reconstruction (next matrix)  ->  O(V^3) time, O(V^2) space
"""

# TODO: implement your solution here