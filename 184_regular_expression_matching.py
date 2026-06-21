"""
184_regular_expression_matching

Question:
Implement regex with '.' and '*'.

Input: s='aa', p='a*'
Output: True

Approaches:
  1. Recursion + memoization on (i,j)  ->  O(m*n) time, O(m*n) space
  2. Bottom-up DP table  ->  O(m*n) time, O(m*n) space
  3. NFA simulation  ->  O(m*n) time, O(n) space
"""

# TODO: implement your solution here