"""
095_copy_list_with_random_pointer

Question:
Deep copy a list with random pointers.

Input: head = [[7,null],[13,0],...]
Output: deep copy

Approaches:
  1. Hash map old->new node, two passes  ->  O(n) time, O(n) space
  2. Interleave copied nodes, set randoms, split  ->  O(n) time, O(1) extra space
"""

# TODO: implement your solution here