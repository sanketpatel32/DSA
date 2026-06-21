"""
010_fibonacci_number

Question:
Compute F(n) where F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).

Input: n = 10
Output: 55

Approaches:
  1. Naive recursion (exponential)  ->  O(2^n) time, O(n) stack
  2. Recursion + memoization (top-down DP)  ->  O(n) time, O(n) space
  3. Iterative bottom-up DP  ->  O(n) time, O(1) space
  4. Matrix exponentiation  ->  O(log n) time, O(1) space
  5. Binet's formula (closed form via golden ratio)  ->  O(log n) (precision-limited) time, O(1) space
  6. Fast doubling identities  ->  O(log n) time, O(1) space
"""

# TODO: implement your solution here