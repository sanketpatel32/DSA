"""
147_insert_interval

Question:
Insert a new interval, merging as needed.

Input: intervals=[[1,3],[6,9]], newInterval=[2,5]
Output: [[1,5],[6,9]]

Approaches:
  1. Linear three-phase: add before, merge overlaps, add after  ->  O(n) time, O(n) space
  2. Append then re-sort and merge  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here