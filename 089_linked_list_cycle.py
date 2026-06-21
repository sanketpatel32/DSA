"""
089_linked_list_cycle

Question:
Return True if the linked list has a cycle.

Input: head = [3,2,0,-4] (cycle)
Output: True

Approaches:
  1. Hash set of visited nodes  ->  O(n) time, O(n) space
  2. Floyd's tortoise and hare (slow/fast)  ->  O(n) time, O(1) space
  3. Mark visited nodes (destructive)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here