"""
132_serialize_and_deserialize_binary_tree

Question:
Serialize tree to string and deserialize back.

Input: root = [1,2,3,null,null,4,5]
Output: round-trips

Approaches:
  1. Preorder with markers for nulls (recursion)  ->  O(n) time, O(n) space
  2. Level order (BFS) serialization  ->  O(n) time, O(n) space
  3. Postorder with null markers  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here