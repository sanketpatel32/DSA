"""
168_coin_change_ii

Question:
Count combinations summing to amount.

Input: amount=5, coins=[1,2,5]
Output: 4

Approaches:
  1. Recursion + memoization  ->  O(n*amount) time, O(n*amount) space
  2. Bottom-up DP (unbounded knapsack)  ->  O(n*amount) time, O(amount) space
"""

# TODO: implement your solution here