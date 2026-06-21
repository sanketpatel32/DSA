"""
085_split_array_largest_sum

Question:
Split into m contiguous subarrays minimizing the largest sum.

Input: nums=[7,2,5,10,8], m=2
Output: 18

Approaches:
  1. Dynamic programming dp[i][j]  ->  O(n^2 * m) time, O(n*m) space
  2. Binary search on the largest sum + greedy feasibility  ->  O(n log sum) time, O(1) space
"""

# TODO: implement your solution here