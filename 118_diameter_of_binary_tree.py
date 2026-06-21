"""
118_diameter_of_binary_tree

Question:
Return the length (edges) of the longest path between any two nodes.

Input: root = [1,2,3,4,5]
Output: 3

Approaches:
  1. Recursion returning height, updating max diameter  ->  O(n) time, O(h) space
  2. Two passes computing height then diameter  ->  O(n^2) time (naive)
"""

# TODO: implement your solution here