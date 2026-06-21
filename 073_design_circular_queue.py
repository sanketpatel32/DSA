"""
073_design_circular_queue

Question:
Design a fixed-size circular queue (en/dequeue, Front/Rear).

Input: k=3, enqueue(1), enqueue(2), Front()
Output: 1

Approaches:
  1. Array with front pointer and size counter  ->  O(1) per op, O(k) space
  2. Array with front and rear pointers (no size, mod arithmetic)  ->  O(1) per op, O(k) space
  3. Linked list with head/tail  ->  O(1) per op, O(k) space
"""

# TODO: implement your solution here