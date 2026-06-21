"""
178_longest_common_subsequence

Question:
Length of LCS of two strings.

Input: text1='abcde', text2='ace'
Output: 3

Approaches:
  1. Recursion + memoization  ->  O(m*n) time, O(m*n) space
  2. Bottom-up DP 2D table  ->  O(m*n) time, O(m*n) space
  3. Bottom-up DP with two rolling rows  ->  O(m*n) time, O(min(m,n)) space
"""

# TODO: implement your solution here