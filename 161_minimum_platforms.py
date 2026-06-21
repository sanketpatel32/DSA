"""
161_minimum_platforms

Question:
Min platforms so no train waits.

Input: arr=[900,940,...], dep=[...]
Output: 3

Approaches:
  1. Sort arrivals and departures, two-pointer merge counting  ->  O(n log n) time, O(n) space
  2. Chronological event counter  ->  O(n log n) time, O(n) space
  3. Min-heap of departure times  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here