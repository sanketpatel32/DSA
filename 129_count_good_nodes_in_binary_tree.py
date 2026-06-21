"""
129_count_good_nodes_in_binary_tree

Question:
Count nodes where no ancestor has a greater value.

Input: root = [3,1,4,3,null,1,5]
Output: 4

Approaches:
  1. DFS tracking the max-so-far on the path  ->  O(n) time, O(h) space
  2. BFS tracking max-so-far per node  ->  O(n) time, O(w) space
"""

# TODO: implement your solution here