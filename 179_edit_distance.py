"""
179_edit_distance

Question:
Min insert/delete/replace to convert word1 to word2.

Input: word1='horse', word2='ros'
Output: 3

Approaches:
  1. Recursion + memoization  ->  O(m*n) time, O(m*n) space
  2. Bottom-up DP 2D table  ->  O(m*n) time, O(m*n) space
  3. Bottom-up DP with two rolling rows  ->  O(m*n) time, O(n) space
"""

# TODO: implement your solution here