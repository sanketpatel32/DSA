"""
232_range_minimum_query

Question:
Answer range minimum queries.

Input: arr=[1,3,2,5,4], query(1,3)
Output: 2

Approaches:
  1. Naive scan per query  ->  O(n) per query, O(1) preprocess
  2. Sparse Table (idempotent, no updates)  ->  O(n log n) preprocess, O(1) query, O(n log n) space
  3. Segment Tree  ->  O(n) preprocess, O(log n) query, O(n) space
  4. Sqrt decomposition  ->  O(n) preprocess, O(sqrt n) query
"""

# TODO: implement your solution here