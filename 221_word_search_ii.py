"""
221_word_search_ii

Question:
All words from list that can be formed in the board.

Input: board=[...], words=['oa','oaa']
Output: ['oa','oaa']

Approaches:
  1. DFS from each cell for each word  ->  O(W * m*n * 4^L) time
  2. Trie of all words + DFS pruning on board  ->  O(m*n * 4^L) time, O(W*L) space
  3. Trie with word removal during DFS for dedup  ->  O(m*n * 4^L) time, O(W*L) space
"""

# TODO: implement your solution here