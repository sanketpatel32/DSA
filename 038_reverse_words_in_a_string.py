"""
038_reverse_words_in_a_string

Question:
Reverse word order, single-spaced, no leading/trailing spaces.

Input: s = 'the sky is blue'
Output: 'blue is sky the'

Approaches:
  1. Built-in split, reverse, join  ->  O(n) time, O(n) space
  2. Manual two-pass: reverse whole, reverse each word, squeeze spaces  ->  O(n) time, O(n) or O(1) space
  3. Deque pushing words from front  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here