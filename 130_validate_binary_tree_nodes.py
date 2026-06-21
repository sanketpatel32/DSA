"""
130_validate_binary_tree_nodes

Question:
Given leftChild/rightChild arrays, check if they form a valid tree.

Input: n=4, leftChild=[1,-1,3,-1], rightChild=[2,-1,-1,-1]
Output: True

Approaches:
  1. Find root (no parent), check single root, no cycles via DFS/BFS  ->  O(n) time, O(n) space
  2. Union-Find with cycle and connectivity checks  ->  O(n a(n)) time, O(n) space
"""

# TODO: implement your solution here