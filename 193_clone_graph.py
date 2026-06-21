"""
193_clone_graph

Question:
Deep copy an undirected connected graph.

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: deep copy

Approaches:
  1. DFS with hash map old->new  ->  O(n) time, O(n) space
  2. BFS with hash map old->new  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here