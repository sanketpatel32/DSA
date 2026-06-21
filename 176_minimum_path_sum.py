"""
176_minimum_path_sum

Question:
Min path sum from top-left to bottom-right.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7

Approaches:
  1. Recursion + memoization  ->  O(m*n) time, O(m*n) space
  2. Bottom-up DP in place  ->  O(m*n) time, O(1) extra space
  3. Bottom-up DP with rolling row  ->  O(m*n) time, O(n) space
"""

# TODO: implement your solution here