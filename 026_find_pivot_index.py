"""
026_find_pivot_index

Question:
Find index where left sum equals right sum.

Input: nums = [1,7,3,6,5,6]
Output: 3

Approaches:
  1. Brute force: recompute sums each index  ->  O(n^2) time, O(1) space
  2. Total sum minus prefix and current element  ->  O(n) time, O(1) space
  3. Prefix sum arrays  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here