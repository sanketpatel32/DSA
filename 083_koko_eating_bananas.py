"""
083_koko_eating_bananas

Question:
Minimum eating speed k to finish all piles within h hours.

Input: piles = [3,6,7,11], h = 8
Output: 4

Approaches:
  1. Linear search speed 1..max(piles)  ->  O(n * max) time
  2. Binary search on speed in [1, max(piles)]  ->  O(n log max) time, O(1) space
"""

# TODO: implement your solution here