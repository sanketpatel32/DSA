"""
187_burst_balloons

Question:
Maximize coins: bursting i gives nums[i-1]*nums[i]*nums[i+1].

Input: nums = [3,1,5,8]
Output: 167

Approaches:
  1. Interval DP dp[i][j] = max coins in (i,j) choosing last burst  ->  O(n^3) time, O(n^2) space
  2. Recursion + memoization on (left,right)  ->  O(n^3) time, O(n^2) space
"""

# TODO: implement your solution here