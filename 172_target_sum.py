"""
172_target_sum

Question:
Assign +/- to reach target S; count ways.

Input: nums=[1,1,1,1,1], target=3
Output: 5

Approaches:
  1. Recursion + memoization  ->  O(n*sum) time, O(n*sum) space
  2. Bottom-up DP (reduce to subset sum)  ->  O(n*sum) time, O(sum) space
"""

# TODO: implement your solution here