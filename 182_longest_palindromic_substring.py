"""
182_longest_palindromic_substring

Question:
Longest palindromic substring.

Input: s = 'babad'
Output: 'bab'

Approaches:
  1. Brute force check all substrings  ->  O(n^3) time, O(1) space
  2. Expand around each center (odd+even)  ->  O(n^2) time, O(1) space
  3. Bottom-up DP table of palindromes  ->  O(n^2) time, O(n^2) space
  4. Manacher's algorithm  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here