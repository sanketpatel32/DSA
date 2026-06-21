"""
100_tower_of_hanoi

Question:
Move n disks from source to destination using auxiliary.

Input: n = 3
Output: 7 moves

Approaches:
  1. Recursion: move n-1 to aux, move largest, move n-1 to dest  ->  O(2^n) moves, O(n) stack
  2. Iterative with parity rules  ->  O(2^n) moves, O(1) space
"""

# TODO: implement your solution here