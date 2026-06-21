"""
013_contains_duplicate

Question:
Return True if any value appears at least twice.

Input: nums = [1,2,3,1]
Output: True

Approaches:
  1. Brute force: all pairs  ->  O(n^2) time, O(1) space
  2. Sort then check adjacent equals  ->  O(n log n) time, O(1) (or O(n)) space
  3. Hash set membership check  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here