"""
071_implement_queue_using_stacks

Question:
Implement a queue using two stacks.

Input: push(1), push(2), peek(), pop()
Output: 1, 1

Approaches:
  1. Two stacks, lazy transfer on pop/peek  ->  O(1) amortized per op, O(n) space
  2. Two stacks, eager transfer on every push  ->  O(n) push, O(1) pop, O(n) space
"""

# TODO: implement your solution here