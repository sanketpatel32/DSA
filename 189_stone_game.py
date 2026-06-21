"""
189_stone_game

Question:
Return True if first player wins picking from ends.

Input: piles = [5,3,4,5]
Output: True

Approaches:
  1. Math (sum of odd vs even indices; first always wins if total odd)  ->  O(1) time, O(1) space
  2. Minimax DP dp[i][j] = max (Alex-Lee) on range  ->  O(n^2) time, O(n^2) space
  3. Recursion + memoization  ->  O(n^2) time, O(n^2) space
"""

# TODO: implement your solution here