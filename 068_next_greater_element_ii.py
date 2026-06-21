"""
068_next_greater_element_ii

Question:
Circular array: next greater for each index.

Input: nums = [1,2,1]
Output: [2,-1,2]

Approaches:
  1. Brute force doubling the array  ->  O(n^2) time
  2. Monotonic stack iterating 2n with mod index  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here