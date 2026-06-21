"""
192_flood_fill

Question:
Starting at (sr,sc), recolor connected same-color pixels.

Input: image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
Output: filled

Approaches:
  1. DFS recursion marking visited  ->  O(m*n) time, O(m*n) stack
  2. BFS with queue  ->  O(m*n) time, O(m*n) space
  3. Iterative DFS with stack  ->  O(m*n) time, O(m*n) space
"""

# TODO: implement your solution here