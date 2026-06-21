"""
110_word_search

Question:
Return True if word exists in board moving to adjacent cells.

Input: board=[...], word='ABCCED'
Output: True

Approaches:
  1. Brute force DFS from each cell without memo  ->  O(n*m*4^L) time, O(L) space
  2. DFS + backtrack (mark visited in-place)  ->  O(n*m*4^L) time, O(L) space
  3. Trie of words then DFS (used in Word Search II)  ->  O(n*m*4^L) time
"""

# TODO: implement your solution here