"""
134_insert_into_a_binary_search_tree

Question:
Insert val into BST; return root.

Input: root=[4,2,7,1,3], val=5
Output: [4,2,7,1,3,5]

Approaches:
  1. Recursion attaching at the correct leaf  ->  O(h) time, O(h) stack
  2. Iteration with trailing parent pointer  ->  O(h) time, O(1) space
"""

# TODO: implement your solution here