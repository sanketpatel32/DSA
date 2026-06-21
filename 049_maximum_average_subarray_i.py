"""
049_maximum_average_subarray_i

Question:
Find max average of a contiguous subarray of length k.

Input: nums=[1,12,-5,-6,50,3], k=4
Output: 12.75

Approaches:
  1. Naive: recompute sum for each window  ->  O(n*k) time, O(1) space
  2. Sliding window: maintain running sum, update on slide  ->  O(n) time, O(1) space
  3. Prefix sums  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here