"""
180_distinct_subsequences

Question:
Count subsequences of s equal to t.

Input: s='rabbbit', t='rabbit'
Output: 3

Approaches:
  1. Recursion + memoization  ->  O(m*n) time, O(m*n) space
  2. Bottom-up DP 2D table  ->  O(m*n) time, O(m*n) space
  3. Bottom-up DP with rolling row  ->  O(m*n) time, O(n) space
"""

# TODO: implement your solution here