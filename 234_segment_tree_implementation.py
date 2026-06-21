"""
234_segment_tree_implementation

Question:
Implement a Segment Tree (range query + update).

Input: arr=[1,3,5,7,9,11]
Output: queries

Approaches:
  1. Recursive segment tree (build/query/update)  ->  O(log n) query/update, O(n) space
  2. Iterative segment tree (array-based)  ->  O(log n) query/update, O(2n) space
  3. Lazy propagation for range updates  ->  O(log n) query/update, O(n) space
"""

# TODO: implement your solution here