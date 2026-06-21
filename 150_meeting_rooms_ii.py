"""
150_meeting_rooms_ii

Question:
Minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Approaches:
  1. Min-heap of end times  ->  O(n log n) time, O(n) space
  2. Separate sorted start/end two-pointer  ->  O(n log n) time, O(n) space
  3. Chronological event counter (+1 start, -1 end)  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here