"""
053_permutation_in_string

Question:
Return True if s2 contains a permutation of s1 as substring.

Input: s1='ab', s2='eidbaooo'
Output: True

Approaches:
  1. Generate all permutations of s1 and search  ->  O(s1! * n) time
  2. Sort s1 and compare every s2 window sorted  ->  O(n * k log k) time
  3. Fixed sliding window with frequency arrays (26)  ->  O(n) time, O(1) space
  4. Sliding window with match counter (no recompare)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here