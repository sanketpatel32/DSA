"""
109_palindrome_partitioning

Question:
Partition so every substring is a palindrome; return all.

Input: s = 'aab'
Output: [['a','a','b'],['aa','b']]

Approaches:
  1. Backtracking with naive palindrome check  ->  O(n*2^n) time, O(n) space
  2. Backtracking with precomputed palindrome table  ->  O(n^2 + n*2^n) time, O(n^2) space
"""

# TODO: implement your solution here