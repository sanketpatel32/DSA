"""
047_4sum

Question:
Find all unique quadruplets summing to target.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: quadruplets

Approaches:
  1. Brute force four loops  ->  O(n^4) time
  2. Hash set generalization of 3sum  ->  O(n^3) time, O(n) space
  3. Sort + two nested loops + two-pointer  ->  O(n^3) time, O(1) extra space
"""

# TODO: implement your solution here