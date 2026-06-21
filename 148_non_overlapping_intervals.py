"""
148_non_overlapping_intervals

Question:
Min intervals to remove to make rest non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

Approaches:
  1. Sort by start, greedy keep earlier-ending  ->  O(n log n) time, O(1) space
  2. Sort by end, count overlaps  ->  O(n log n) time, O(1) space
  3. DP after sorting by start  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here