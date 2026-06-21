"""
063_valid_parentheses

Question:
Return True if bracket string is valid.

Input: s = '()[]{}'
Output: True

Approaches:
  1. Stack push/pop matching openers with closers  ->  O(n) time, O(n) space
  2. Counter-only variant (only one bracket type)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here