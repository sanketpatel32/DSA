"""
218_design_add_and_search_words_data_structure

Question:
Trie supporting '.' wildcard in search.

Input: addWord('bad'), search('.ad')
Output: True

Approaches:
  1. Trie with DFS on wildcard (try all children at '.')  ->  O(L) insert / O(26^L) worst-case search, O(N*L) space
  2. Length-bucketed hash set + regex match per query  ->  O(L) insert / O(N*L) search
"""

# TODO: implement your solution here