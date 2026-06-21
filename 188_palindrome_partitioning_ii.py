"""
188_palindrome_partitioning_ii

Question:
Min cuts to partition s into palindromes.

Input: s = 'aab'
Output: 1

Approaches:
  1. DP cuts[i] = min cuts for prefix; check palindrome each step  ->  O(n^2) time, O(n^2) space
  2. DP with expand-from-center palindrome detection  ->  O(n^2) time, O(n) space
"""

# TODO: implement your solution here