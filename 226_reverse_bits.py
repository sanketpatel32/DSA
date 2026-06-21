"""
226_reverse_bits

Question:
Reverse the 32 bits of an unsigned integer.

Input: n = 43261596
Output: 964176192

Approaches:
  1. Bit-by-bit shift and accumulate over 32 positions  ->  O(1) (32 iterations) time, O(1) space
  2. Byte-swap with precomputed reverse lookup table  ->  O(1) time, O(256) space
  3. Mask and shift halves (divide and conquer)  ->  O(1) time, O(1) space
"""

# TODO: implement your solution here