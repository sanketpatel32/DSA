"""
125_binary_tree_zigzag_level_order_traversal

Question:
Level order alternating direction per level.

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Approaches:
  1. BFS with reverse every other level  ->  O(n) time, O(w) space
  2. BFS with deque appending front/back alternately  ->  O(n) time, O(w) space
  3. Two stacks for alternate directions  ->  O(n) time, O(w) space
"""

# TODO: implement your solution here