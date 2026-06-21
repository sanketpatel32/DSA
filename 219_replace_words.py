"""
219_replace_words

Question:
Replace words with shortest matching root.

Input: dictionary=['cat','bat','rat'], sentence='the cattle...'
Output: replaced

Approaches:
  1. Trie of roots; walk each word stopping at first root  ->  O(n*L) time, O(n*L) space
  2. Hash set checking all prefixes of each word  ->  O(n*L^2) time, O(n*L) space
  3. Sort roots by length, check membership  ->  O(n log n * L) time
"""

# TODO: implement your solution here