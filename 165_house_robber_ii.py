"""
165_house_robber_ii

Question:
Same as House Robber but houses are circular.

Input: nums = [2,3,2]
Output: 3

Approaches:
  1. Two runs of House Robber: exclude first / exclude last  ->  O(n) time, O(1) space
  2. DP on both segments  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here