"""
027_subarray_sum_equals_k

Question:
Count continuous subarrays whose sum equals k.

Input: nums = [1,1,1], k = 2
Output: 2

Approaches:
  1. Brute force: all subarrays with running sum  ->  O(n^2) time, O(1) space
  2. Prefix sum + hash map of prefix frequencies  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here