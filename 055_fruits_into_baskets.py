"""
055_fruits_into_baskets

Question:
Longest subarray with at most 2 distinct values.

Input: fruits = [1,2,1]
Output: 3

Approaches:
  1. Brute force: all subarrays, count distinct  ->  O(n^2) time
  2. Sliding window with hash map of counts  ->  O(n) time, O(1) space
  3. Sliding window with last occurrence tracking  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here