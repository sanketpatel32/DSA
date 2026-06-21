"""
051_longest_substring_without_repeating_characters

Question:
Length of longest substring without repeating characters.

Input: s = 'abcabcbb'
Output: 3

Approaches:
  1. Brute force: all substrings with set check  ->  O(n^3) or O(n^2) time
  2. Sliding window with set  ->  O(n) time, O(min(n,charset)) space
  3. Sliding window with last-seen index map (jump left)  ->  O(n) time, O(min(n,charset)) space
"""

# TODO: implement your solution here