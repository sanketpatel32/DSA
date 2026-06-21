"""
220_longest_word_in_dictionary

Question:
Longest word buildable by adding one letter at a time.

Input: words = ['w','wo','wor','worl','world']
Output: 'world'

Approaches:
  1. Sort words; BFS/DFS on Trie built incrementally  ->  O(n*L) time, O(n*L) space
  2. Hash set of words; DFS extending by one letter  ->  O(n*L) time, O(n) space
  3. Sort by length then lexicographical; greedy check prefixes  ->  O(n log n * L) time
"""

# TODO: implement your solution here