"""
202_alien_dictionary

Question:
Derive character order from sorted alien words.

Input: words = ['wrt','wrf','er','ett','rftt']
Output: 'wertf'

Approaches:
  1. Build graph from adjacent word pairs, then topological sort  ->  O(C) time, O(1) (26 letters) space
  2. Kahn's BFS topological sort  ->  O(C) time, O(U) space (U unique chars)
"""

# TODO: implement your solution here