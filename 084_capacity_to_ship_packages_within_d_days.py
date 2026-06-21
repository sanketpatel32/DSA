"""
084_capacity_to_ship_packages_within_d_days

Question:
Minimum capacity to ship packages in order within d days.

Input: weights=[1,2,3,4,5,6,7,8,9,10], days=5
Output: 15

Approaches:
  1. Linear search capacity  ->  O(n * sum) time
  2. Binary search on capacity in [max(weights), sum(weights)]  ->  O(n log sum) time, O(1) space
"""

# TODO: implement your solution here