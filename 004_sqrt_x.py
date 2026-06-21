"""
004_sqrt_x

Question:
Given a non-negative integer x, return floor(sqrt(x)).

Input: x = 8
Output: 2

Approaches:
  1. Linear search 1..x  ->  O(sqrt x) time, O(1) space
  2. Binary search on [0, x]  ->  O(log x) time, O(1) space
  3. Newton-Raphson iteration  ->  O(log x) time, O(1) space
  4. Built-in math.isqrt (Python 3.8+)  ->  O(1) (implementation-dependent)
"""

# TODO: implement your solution here