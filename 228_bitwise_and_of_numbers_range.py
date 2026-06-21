"""
228_bitwise_and_of_numbers_range

Question:
Bitwise AND of all numbers in [left,right].

Input: left = 5, right = 7
Output: 4

Approaches:
  1. Brute force AND across range  ->  O(n) time, O(1) space
  2. Right-shift both until equal, then shift back (common prefix)  ->  O(log n) time, O(1) space
  3. Clear lowest set bit of right while right > left  ->  O(log n) time, O(1) space
"""

# TODO: implement your solution here