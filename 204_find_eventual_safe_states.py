"""
204_find_eventual_safe_states

Question:
Nodes eventually leading to a terminal/safe node, sorted.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Approaches:
  1. DFS with three-color marking (safe vs cycle)  ->  O(V+E) time, O(V) space
  2. Reverse topological sort from terminal nodes  ->  O(V+E) time, O(V) space
"""

# TODO: implement your solution here