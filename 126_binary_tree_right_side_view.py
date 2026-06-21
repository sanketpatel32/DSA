"""
126_binary_tree_right_side_view

Question:
Values of nodes visible from the right, top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Approaches:
  1. BFS, take last node of each level  ->  O(n) time, O(w) space
  2. DFS, record first node seen at each depth (right-first)  ->  O(n) time, O(h) space
"""

# TODO: implement your solution here