"""
205_redundant_connection

Question:
In a tree plus one extra edge, return the redundant edge.

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Approaches:
  1. Union-Find (DSU): first edge that already unites two in same set  ->  O(n a(n)) time, O(n) space
  2. DFS cycle detection then locate last edge in cycle  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here