"""
185_best_time_to_buy_and_sell_stock_with_cooldown

Question:
Max profit with 1-day cooldown after each sell.

Input: prices = [1,2,3,0,2]
Output: 3

Approaches:
  1. State-machine DP (held/cold/cooldown states)  ->  O(n) time, O(1) space
  2. Recursion + memoization on (day,state)  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here