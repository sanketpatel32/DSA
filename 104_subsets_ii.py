"""
104_subsets_ii

Question:
Return unique subsets of an array with duplicates.

Input: nums = [1,2,2]
Output: 6 subsets

Approaches:
  1. Backtracking with sort + skip duplicates  ->  O(n*2^n) time, O(n) space
  2. Iterative: count duplicates, extend in groups  ->  O(n*2^n) time
  3. Hash set of tuple subsets to dedupe  ->  O(n*2^n) time, O(n*2^n) space
"""

# TODO: implement your solution here