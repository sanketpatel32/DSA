"""
206_number_of_connected_components_in_an_undirected_graph

Question:
Count connected components in an undirected graph.

Input: n=5, edges=[[0,1],[1,2],[3,4]]
Output: 2

Approaches:
  1. DFS/BFS over all nodes with visited set  ->  O(V+E) time, O(V) space
  2. Union-Find  ->  O(V+E * a(V)) time, O(V) space
"""

# TODO: implement your solution here