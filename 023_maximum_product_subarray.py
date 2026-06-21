"""
023_maximum_product_subarray

Question:
Find the contiguous subarray with the largest product.

Input: nums = [2,3,-2,4]
Output: 6

Approaches:
  1. Brute force: all subarrays  ->  O(n^2) time, O(1) space
  2. Track current min and max (sign flip on negative)  ->  O(n) time, O(1) space
  3. DP with two arrays (min/max ending at i)  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here