"""
167_coin_change

Question:
Fewest coins to make amount, else -1.

Input: coins=[1,2,5], amount=11
Output: 3

Approaches:
  1. Recursion + memoization  ->  O(n*amount) time, O(amount) space
  2. Bottom-up DP (min coins per amount)  ->  O(n*amount) time, O(amount) space
  3. BFS on amounts (each level = one more coin)  ->  O(n*amount) time, O(amount) space
"""

# TODO: implement your solution here