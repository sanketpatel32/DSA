"""
014_best_time_to_buy_and_sell_stock

Question:
Return the maximum profit from one buy-then-sell transaction.

Input: prices = [7,1,5,3,6,4]
Output: 5

Approaches:
  1. Brute force: try every buy/sell pair  ->  O(n^2) time, O(1) space
  2. Single pass: track min price so far and max profit  ->  O(n) time, O(1) space
  3. Dynamic programming (track state)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here