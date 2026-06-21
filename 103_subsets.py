"""
103_subsets

Question:
Return the power set of a distinct-integer array.

Input: nums = [1,2,3]
Output: 8 subsets

Approaches:
  1. Backtracking include/exclude each element  ->  O(n*2^n) time, O(n) space
  2. Iterative: for each element, extend existing subsets  ->  O(n*2^n) time, O(n*2^n) space
  3. Bitmask iteration 0..2^n-1  ->  O(n*2^n) time, O(n*2^n) space
"""

# TODO: implement your solution here