"""
162_climbing_stairs

Question:
Distinct ways to climb 1 or 2 steps to reach n.

Input: n = 3
Output: 3

Approaches:
  1. Recursion (Fibonacci)  ->  O(2^n) time, O(n) stack
  2. Memoization (top-down DP)  ->  O(n) time, O(n) space
  3. Bottom-up DP  ->  O(n) time, O(1) space
  4. Matrix exponentiation  ->  O(log n) time, O(1) space
"""

# TODO: implement your solution here