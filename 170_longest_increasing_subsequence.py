"""
170_longest_increasing_subsequence

Question:
Length of longest strictly increasing subsequence.

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Approaches:
  1. DP: dp[i] = LIS ending at i (compare all j<i)  ->  O(n^2) time, O(n) space
  2. Patience sorting with binary search (tails array)  ->  O(n log n) time, O(n) space
  3. Segment tree / Fenwick on values  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here