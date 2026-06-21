"""
229_power_of_two

Question:
Return True if n is a power of two.

Input: n = 16
Output: True

Approaches:
  1. Repeated division by 2  ->  O(log n) time, O(1) space
  2. Bit check: n > 0 and (n & (n-1)) == 0  ->  O(1) time, O(1) space
  3. Logarithm check (floating point)  ->  O(1) time, O(1) space
  4. Count set bits == 1  ->  O(1) time, O(1) space
"""

# TODO: implement your solution here