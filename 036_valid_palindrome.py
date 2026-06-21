"""
036_valid_palindrome

Question:
Check palindrome considering only alphanumeric, ignoring case.

Input: s = 'A man, a plan, a canal: Panama'
Output: True

Approaches:
  1. Clean string then two-pointer  ->  O(n) time, O(n) space
  2. Two-pointer directly on raw string skipping non-alnum  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here