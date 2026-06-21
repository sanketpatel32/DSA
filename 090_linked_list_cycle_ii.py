"""
090_linked_list_cycle_ii

Question:
Return the node where the cycle begins, or None.

Input: head = [3,2,0,-4] (cycle)
Output: node at index 1

Approaches:
  1. Hash set of visited nodes  ->  O(n) time, O(n) space
  2. Floyd then reset one pointer and walk equal steps  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here