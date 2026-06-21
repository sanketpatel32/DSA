"""
177_triangle

Question:
Min path sum from top to bottom of a triangle.

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11

Approaches:
  1. Top-down DP with memoization  ->  O(n^2) time, O(n^2) space
  2. Bottom-up DP in place (modify triangle)  ->  O(n^2) time, O(1) extra space
  3. Bottom-up DP with 1D array  ->  O(n^2) time, O(n) space
"""

# TODO: implement your solution here