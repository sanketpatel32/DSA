"""
160_maximum_subarray_circular

Question:
Max subarray sum in a circular array.

Input: nums = [1,-2,3,-2]
Output: 3

Approaches:
  1. Kadane on original and on inverted (total - min subarray)  ->  O(n) time, O(1) space
  2. Prefix and suffix max arrays  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here