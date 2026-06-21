"""
223_single_number_ii

Question:
Every element three times except one; find it.

Input: nums = [2,2,3,2]
Output: 3

Approaches:
  1. Hash map frequency count  ->  O(n) time, O(n) space
  2. Sort and scan groups of three  ->  O(n log n) time, O(1) space
  3. Bitwise: count set bits mod 3  ->  O(n) time, O(1) space
  4. Bit manipulation with two masks (ones/twos)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here