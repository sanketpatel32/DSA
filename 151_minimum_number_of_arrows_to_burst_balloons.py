"""
151_minimum_number_of_arrows_to_burst_balloons

Question:
Min arrows to burst all balloons (x-axis intervals).

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2

Approaches:
  1. Sort by end, greedy count non-overlapping groups  ->  O(n log n) time, O(1) space
  2. Sort by start, track arrow position  ->  O(n log n) time, O(1) space
"""

# TODO: implement your solution here