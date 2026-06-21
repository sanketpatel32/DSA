"""
033_isomorphic_strings

Question:
Two strings isomorphic if chars map bijectively.

Input: s = 'egg', t = 'add'
Output: True

Approaches:
  1. Two hash maps (s->t and t->s)  ->  O(n) time, O(1) (charset) space
  2. Single map with value-set check  ->  O(n) time, O(1) space
  3. Translate both to first-occurrence index arrays and compare  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here