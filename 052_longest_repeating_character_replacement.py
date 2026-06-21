"""
052_longest_repeating_character_replacement

Question:
Longest substring where <= k replacements make all chars same.

Input: s = 'AABABBA', k = 1
Output: 4

Approaches:
  1. Brute force: all substrings, count majority  ->  O(n^2) time
  2. Sliding window tracking max char frequency  ->  O(n) time, O(1) space (charset)
  3. Sliding window with counter shrink when invalid  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here