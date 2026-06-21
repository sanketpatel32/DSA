"""
099_kth_symbol_in_grammar

Question:
Row n is row n-1 + flipped; find kth symbol (1-indexed).

Input: n = 1, k = 1
Output: 0

Approaches:
  1. Build all rows up to n  ->  O(2^n) time, O(2^n) space
  2. Recursion: kth symbol depends on parent at (k+1)//2  ->  O(n) time, O(n) stack
  3. Iterative bit-parity of (k-1)  ->  O(log k) time, O(1) space
"""

# TODO: implement your solution here