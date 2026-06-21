"""
106_permutations_ii

Question:
Return all unique permutations of an array with duplicates.

Input: nums = [1,1,2]
Output: 3 permutations

Approaches:
  1. Backtracking with frequency counter  ->  O(n*n!) time, O(n) space
  2. Backtracking with sort + skip same level duplicates  ->  O(n*n!) time, O(n) space
  3. Generate then dedupe via set  ->  O(n*n!) time, O(n*n!) space
"""

# TODO: implement your solution here