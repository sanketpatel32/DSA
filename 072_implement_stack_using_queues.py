"""
072_implement_stack_using_queues

Question:
Implement a stack using queues.

Input: push(1), push(2), top(), pop()
Output: 2, 2

Approaches:
  1. Two queues: rotate after each push so front is top  ->  O(n) push, O(1) pop, O(n) space
  2. One queue: rotate (size-1) after each push  ->  O(n) push, O(1) pop, O(n) space
  3. Two queues: copy on pop  ->  O(1) push, O(n) pop, O(n) space
"""

# TODO: implement your solution here