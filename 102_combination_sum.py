"""
102_combination_sum

Question:
All unique combinations summing to target (unlimited use).

Input: candidates=[2,3,6,7], target=7
Output: [[2,2,3],[7]]

Approaches:
  1. Backtracking with start index, allow reuse  ->  O(2^n) (bounded by target) time
  2. DP counting then reconstruct (less natural for listing)  ->  O(n*target) time
"""

# TODO: implement your solution here