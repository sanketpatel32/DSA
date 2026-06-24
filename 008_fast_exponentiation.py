"""
008_fast_exponentiation

Question:
Compute x^n efficiently using binary exponentiation.

Input: x = 2, n = 10
Output: 1024

Approaches:
  1. Iterative binary exponentiation (square-and-multiply)  ->  O(log n) time, O(1) space
  2. Recursive binary exponentiation  ->  O(log n) time, O(log n) stack
  3. Naive loop multiplying x n times  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here


def recursive_exponentiation(A: int, N: int) -> int:
    if N == 0:
        return 1
    elif N % 2 == 0:
        temp = recursive_exponentiation(A, (N // 2))
        return temp * temp
    else:
        return A*recursive_exponentiation(A, N - 1)
        
print(recursive_exponentiation(3, 5))
