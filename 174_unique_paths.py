"""
174_unique_paths

Question:
Count paths from top-left to bottom-right (right/down).

Input: m=3, n=7
Output: 28

Approaches:
  1. Recursion + memoization  ->  O(m*n) time, O(m*n) space
  2. Bottom-up DP  ->  O(m*n) time, O(n) space
  3. Combinatorics: C(m+n-2, m-1)  ->  O(min(m,n)) time, O(1) space
"""

# TODO: implement your solution here