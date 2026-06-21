"""
012_two_sum

Question:
Given nums and a target, return indices of the two numbers that add up to target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Approaches:
  1. Brute force: check all pairs  ->  O(n^2) time, O(1) space
  2. Sort + two-pointer (loses original indices unless tracked)  ->  O(n log n) time, O(n) space
  3. Hash map (one pass): check complement while iterating  ->  O(n) time, O(n) space
  4. Hash map (two pass): build map then lookup  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here