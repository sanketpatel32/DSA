"""
145_find_median_from_data_stream

Question:
Support addNum and findMedian.

Input: addNum(1), addNum(2), findMedian(), addNum(3), findMedian()
Output: 1.5, 2.0

Approaches:
  1. Sort on each query  ->  O(n log n) per median
  2. Insertion sort insertion  ->  O(n) add, O(1) median
  3. Two heaps: max-heap lower half, min-heap upper half  ->  O(log n) add, O(1) median
  4. Balanced BST / order statistic tree  ->  O(log n) add, O(log n) median
"""

# TODO: implement your solution here