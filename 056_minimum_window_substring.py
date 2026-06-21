"""
056_minimum_window_substring

Question:
Smallest window of s containing all chars of t.

Input: s='ADOBECODEBANC', t='ABC'
Output: 'BANC'

Approaches:
  1. Brute force: all substrings  ->  O(n^2) time
  2. Sliding window with two pointers + frequency map + match counter  ->  O(n+m) time, O(n+m) space
  3. Filtered s + sliding window (only t chars)  ->  O(n+m) time, O(n+m) space
"""

# TODO: implement your solution here