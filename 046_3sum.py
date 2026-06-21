"""
046_3sum

Question:
Find all unique triplets summing to 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Approaches:
  1. Brute force three loops  ->  O(n^3) time, O(1) space
  2. Hash set: two-sum extension for each first element  ->  O(n^2) time, O(n) space
  3. Sort + two-pointer for each first element  ->  O(n^2) time, O(1) extra space
"""

# TODO: implement your solution here