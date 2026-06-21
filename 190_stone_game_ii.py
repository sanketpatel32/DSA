"""
190_stone_game_ii

Question:
Alice and Bob take piles with M rule; return Alice's max stones.

Input: piles = [2,7,9,4,4], M = 1
Output: 10

Approaches:
  1. DP dp[i][m][turn] with suffix sums  ->  O(n^3) time, O(n^2) space
  2. Recursion + memoization on (i,m,turn)  ->  O(n^3) time, O(n^2) space
"""

# TODO: implement your solution here