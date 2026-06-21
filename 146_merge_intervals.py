"""
146_merge_intervals

Question:
Merge all overlapping intervals.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Approaches:
  1. Sort by start then merge sequentially  ->  O(n log n) time, O(n) space
  2. Connected components / graph approach  ->  O(n^2) time, O(n^2) space
"""

# TODO: implement your solution here