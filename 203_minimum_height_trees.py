"""
203_minimum_height_trees

Question:
Root labels of Minimum Height Trees (centroids).

Input: n=4, edges=[[1,0],[1,2],[1,3]]
Output: [1]

Approaches:
  1. BFS from each node computing height (brute)  ->  O(V*(V+E)) time, O(V) space
  2. Leaf-peeling (topological) toward centroids  ->  O(V) time, O(V) space
"""

# TODO: implement your solution here