"""
164_house_robber

Question:
Cannot rob adjacent houses; maximize total.

Input: nums = [1,2,3,1]
Output: 4

Approaches:
  1. Recursion + memoization  ->  O(n) time, O(n) space
  2. Bottom-up DP array (rob[i] = max(rob[i-1], rob[i-2]+nums[i]))  ->  O(n) time, O(n) space
  3. Bottom-up DP with two variables  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here