"""
183_palindromic_substrings

Question:
Count palindromic substrings.

Input: s = 'aaa'
Output: 6

Approaches:
  1. Brute force check all substrings  ->  O(n^3) time, O(1) space
  2. Expand around center for each position  ->  O(n^2) time, O(1) space
  3. Bottom-up DP table  ->  O(n^2) time, O(n^2) space
  4. Manacher's algorithm  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here