"""
231_range_sum_query_mutable

Question:
Point updates and range sum queries.

Input: nums=[1,3,5], update(1,2), sumRange(0,2)
Output: 8

Approaches:
  1. Naive array, recompute sum per query  ->  O(1) update, O(n) query
  2. Prefix sum (rebuild on update)  ->  O(n) update, O(1) query
  3. Fenwick Tree (Binary Indexed Tree)  ->  O(log n) update/query, O(n) space
  4. Segment Tree  ->  O(log n) update/query, O(n) space
  5. Sqrt decomposition (block sums)  ->  O(sqrt n) update/query, O(n) space
"""

# TODO: implement your solution here