"""
007_gcd_and_lcm

Question:
Given two positive integers a and b, compute their GCD and LCM.

Input: a = 12, b = 18
Output: GCD = 6, LCM = 36

Approaches:
  1. Euclidean algorithm (iterative)  ->  O(log(min(a,b))) time, O(1) space
  2. Euclidean algorithm (recursive)  ->  O(log(min(a,b))) time, O(log(min(a,b))) stack
  3. Stein's algorithm (binary GCD, bitwise)  ->  O(log(min(a,b))) time, O(1) space
  4. LCM = a*b / GCD(a,b)  ->  O(log(min(a,b))) time
"""

# TODO: implement your solution here