"""
087_reverse_linked_list

Question:
Reverse a singly linked list; return new head.

Input: 1->2->3->4->5
Output: 5->4->3->2->1

Approaches:
  1. Iterative three-pointer (prev/curr/next)  ->  O(n) time, O(1) space
  2. Recursive returning new head  ->  O(n) time, O(n) stack
  3. Stack-based node reversal  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here