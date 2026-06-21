"""
208_graph_valid_tree

Question:
Check if n nodes and edges form a valid tree.

Input: n=5, edges=[[0,1],[0,2],[0,3],[1,4]]
Output: True

Approaches:
  1. DFS/BFS: connected + exactly n-1 edges + no cycle  ->  O(V+E) time, O(V) space
  2. Union-Find: all unite and no cycle  ->  O(V+E * a) time, O(V) space
"""

# TODO: implement your solution here