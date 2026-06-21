"""
156_jump_game_ii

Question:
Return minimum jumps to reach last index.

Input: nums = [2,3,1,1,4]
Output: 2

Approaches:
  1. DP from right  ->  O(n^2) time, O(n) space
  2. BFS-like level traversal of jump ranges  ->  O(n) time, O(1) space
  3. Greedy with current-jump-end pointer  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here