"""
173_combination_sum_iv

Question:
Count ordered combinations summing to target.

Input: nums=[1,2,3], target=4
Output: 7

Approaches:
  1. Recursion + memoization  ->  O(n*target) time, O(target) space
  2. Bottom-up DP dp[i] = sum dp[i-num]  ->  O(n*target) time, O(target) space
"""

# TODO: implement your solution here