"""
107_combination_sum_ii

Question:
Unique combinations summing to target; each number once.

Input: candidates=[10,1,2,7,6,1,5], target=8
Output: combinations

Approaches:
  1. Backtracking with sort + skip duplicates at same level  ->  O(2^n) time, O(n) space
  2. Counter-based backtracking on unique values  ->  O(2^n) time, O(n) space
"""

# TODO: implement your solution here