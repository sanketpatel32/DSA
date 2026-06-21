"""
043_valid_palindrome_ii

Question:
Check if string can be a palindrome after deleting at most one char.

Input: s = 'abca'
Output: True

Approaches:
  1. Brute force: try deleting each char and check palindrome  ->  O(n^2) time, O(1) space
  2. Two-pointer; on mismatch, skip either side and recheck  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here