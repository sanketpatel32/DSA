"""
141_last_stone_weight

Question:
Smash two heaviest stones each turn; return last weight or 0.

Input: stones = [2,7,4,1,8,1]
Output: 1

Approaches:
  1. Max-heap (negate for Python heap)  ->  O(n log n) time, O(n) space
  2. Sort each round  ->  O(n^2 log n) time, O(1) space
"""

# TODO: implement your solution here