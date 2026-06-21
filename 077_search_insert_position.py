"""
077_search_insert_position

Question:
Return index of target or where it would be inserted.

Input: nums=[1,3,5,6], target=5
Output: 2

Approaches:
  1. Linear scan  ->  O(n) time, O(1) space
  2. Binary search for lower bound  ->  O(log n) time, O(1) space
  3. bisect_left  ->  O(log n) time, O(1) space
"""

# TODO: implement your solution here