"""
225_number_of_1_bits

Question:
Number of set bits of an unsigned integer.

Input: n = 11
Output: 3

Approaches:
  1. Right-shift loop checking LSB  ->  O(k) time, O(1) space
  2. Brian Kernighan's: n &= n-1 counts only set bits  ->  O(number of set bits) time, O(1) space
  3. Built-in bin(n).count('1') or int.bit_count()  ->  O(1) time
"""

# TODO: implement your solution here