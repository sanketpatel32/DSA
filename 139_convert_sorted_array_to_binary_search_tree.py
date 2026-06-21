"""
139_convert_sorted_array_to_binary_search_tree

Question:
Convert sorted array into a height-balanced BST.

Input: nums = [-10,-3,0,5,9]
Output: balanced BST

Approaches:
  1. Recursion: middle as root, recurse on halves  ->  O(n) time, O(log n) space
  2. Iteration with explicit stack of (lo,hi) ranges  ->  O(n) time, O(log n) space
"""

# TODO: implement your solution here