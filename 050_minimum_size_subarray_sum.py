"""
050_minimum_size_subarray_sum

Question:
Minimal length of contiguous subarray with sum >= target.

Input: target=7, nums=[2,3,1,2,4,3]
Output: 2

Approaches:
  1. Brute force: all subarrays  ->  O(n^2) time, O(1) space
  2. Prefix sum + binary search on prefix  ->  O(n log n) time, O(n) space
  3. Variable-size sliding window (two-pointer)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here