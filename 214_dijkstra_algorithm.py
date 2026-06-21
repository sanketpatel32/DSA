"""
214_dijkstra_algorithm

Question:
Shortest paths from source to all nodes (non-negative weights).

Input: weighted graph, source = 0
Output: distance array

Approaches:
  1. Min-heap Dijkstra  ->  O(E log V) time, O(V) space
  2. Array-based Dijkstra (linear min search)  ->  O(V^2) time, O(V) space
  3. Lazy deletion variant  ->  O(E log V) time, O(V) space
"""

# TODO: implement your solution here