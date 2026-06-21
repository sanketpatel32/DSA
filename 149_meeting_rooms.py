"""
149_meeting_rooms

Question:
Return True if a person can attend all meetings.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: False

Approaches:
  1. Brute force: check all pairs for overlap  ->  O(n^2) time, O(1) space
  2. Sort by start then check adjacent  ->  O(n log n) time, O(1) space
  3. Chronological ordering of start/end events  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here