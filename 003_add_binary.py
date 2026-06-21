"""
003_add_binary

Question:
Given two binary strings a and b, return their sum as a binary string.

Input: a = '11', b = '1'
Output: '100'

Approaches:
  1. Bit-by-bit simulation from right with carry  ->  O(max(n,m)) time, O(max(n,m)) space
  2. Convert to int, sum, format back to binary (Python int(a,2))  ->  O(max(n,m)) time, O(max(n,m)) space  (limited by int width)
  3. Bit manipulation without full string conversion  ->  O(max(n,m)) time, O(max(n,m)) space
"""

# TODO: implement your solution here