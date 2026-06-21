"""
153_assign_cookies

Question:
Assign cookies to maximize content children.

Input: g=[1,2,3], s=[1,1]
Output: 1

Approaches:
  1. Sort both, two-pointer greedy assign smallest sufficient cookie  ->  O(n log n + m log m) time, O(1) space
  2. Brute force: try every cookie for every child  ->  O(n*m) time
"""

# TODO: implement your solution here