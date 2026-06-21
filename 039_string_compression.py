"""
039_string_compression

Question:
Compress char array in-place using counts; return new length.

Input: chars = ['a','a','b','b','c','c','c']
Output: 6, ['a','2','b','2','c','3']

Approaches:
  1. Two-pointer: read groups, write chars and counts  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here