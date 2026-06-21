"""
152_employee_free_time

Question:
Return common free intervals given schedules.

Input: schedule=[[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]

Approaches:
  1. Flatten all intervals, sort, merge, find gaps  ->  O(n log n) time, O(n) space
  2. Min-heap of (start,end,interval_index)  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here