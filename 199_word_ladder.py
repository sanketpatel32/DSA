"""
199_word_ladder

Question:
Shortest transformation length from beginWord to endWord.

Input: beginWord='hit', endWord='cog', wordList=[...]
Output: 5

Approaches:
  1. BFS on words (neighbors via wildcard patterns)  ->  O(n * L^2) time, O(n) space
  2. Bidirectional BFS from both ends  ->  O(n * L^2) time (faster), O(n) space
  3. Build adjacency via intermediate generic forms  ->  O(n * L^2) time, O(n*L^2) space
"""

# TODO: implement your solution here