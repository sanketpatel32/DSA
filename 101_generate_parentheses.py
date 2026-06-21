"""
101_generate_parentheses

Question:
Generate all well-formed combinations of n pairs.

Input: n = 3
Output: 5 strings

Approaches:
  1. Brute force all 2^(2n) strings, validate  ->  O(2^(2n) * n) time
  2. Backtracking with open/close counts  ->  O(4^n / sqrt(n)) time, O(n) space
  3. Closure number recursion  ->  O(4^n / sqrt(n)) time, O(n) space
"""

# TODO: implement your solution here