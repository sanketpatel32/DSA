"""
009_pow_x_n

Question:
Implement pow(x, n) computing x raised to the power n.

Input: x = 2.0, n = 10
Output: 1024.0

Approaches:
  1. Iterative binary exponentiation (handle negative n via 1/x)  ->  O(log n) time, O(1) space
  2. Recursive binary exponentiation  ->  O(log n) time, O(log n) stack
  3. Naive multiplication  ->  O(n) time, O(1) space
  4. Built-in x**n or math.pow  ->  O(1) (implementation-dependent)
"""

# TODO: implement your solution here