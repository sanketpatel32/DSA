"""
034_word_pattern

Question:
Check if string s follows the same bijection as pattern.

Input: pattern='abba', s='dog cat cat dog'
Output: True

Approaches:
  1. Two hash maps (pattern char -> word, word -> char)  ->  O(n) time, O(n) space
  2. Single map plus set of seen words  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here