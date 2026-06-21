"""
166_decode_ways

Question:
Count ways to decode digit string ('1'->'A'...).

Input: s = '226'
Output: 3

Approaches:
  1. Recursion + memoization  ->  O(n) time, O(n) space
  2. Bottom-up DP (1 or 2 digit transitions)  ->  O(n) time, O(n) space
  3. Bottom-up DP with two variables  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here