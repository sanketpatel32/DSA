"""
032_happy_number

Question:
Replace n by sum of squares of its digits; return True if it reaches 1.

Input: n = 19
Output: True

Approaches:
  1. Hash set to detect cycle  ->  O(log n) time, O(log n) space
  2. Floyd's cycle detection (slow/fast pointers)  ->  O(log n) time, O(1) space
"""

# TODO: implement your solution here