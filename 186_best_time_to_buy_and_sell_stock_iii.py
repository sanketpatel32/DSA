"""
186_best_time_to_buy_and_sell_stock_iii

Question:
Max profit with at most 2 transactions.

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6

Approaches:
  1. State-machine DP with 4 states (buy1/sell1/buy2/sell2)  ->  O(n) time, O(1) space
  2. DP table [day][transactions used][holding]  ->  O(n*k) time, O(n*k) space
  3. Divide-and-conquer with prefix/suffix max arrays  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here