"""
035_valid_anagram

Question:
Return True if t is an anagram of s.

Input: s = 'anagram', t = 'nagaram'
Output: True

Approaches:
  1. Sort both strings and compare  ->  O(n log n) time, O(n) space
  2. Frequency count arrays (26)  ->  O(n) time, O(1) space
  3. Hash map counters  ->  O(n) time, O(k) space
  4. Counter (collections.Counter) equality  ->  O(n) time, O(k) space
"""

# TODO: implement your solution here