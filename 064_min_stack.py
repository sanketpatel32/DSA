"""
064_min_stack

Question:
Stack supporting push, pop, top, getMin in O(1).

Input: push(-2), push(0), push(-3), getMin()
Output: -3

Approaches:
  1. Auxiliary stack mirroring current minimum  ->  O(1) per op, O(n) space
  2. Store (value, running_min) tuples on one stack  ->  O(1) per op, O(n) space
  3. Two-stack with deduplicated min stack  ->  O(1) per op, O(n) space
"""

# TODO: implement your solution here