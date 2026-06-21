"""
028_continuous_subarray_sum

Question:
Return True if a subarray of size >=2 has sum divisible by k.

Input: nums = [23,2,4,6,7], k = 6
Output: True

Approaches:
  1. Brute force: all subarrays  ->  O(n^2) time, O(1) space
  2. Prefix remainder + hash map of earliest index  ->  O(n) time, O(min(n,k)) space
"""

# TODO: implement your solution here