"""
016_missing_number

Question:
Array of n distinct numbers from 0..n. Find the missing one.

Input: nums = [3,0,1]
Output: 2

Approaches:
  1. Brute force: check each number 0..n  ->  O(n^2) time, O(1) space
  2. Hash set membership  ->  O(n) time, O(n) space
  3. Sort then scan for gap  ->  O(n log n) time, O(1) space
  4. Math: expected sum n(n+1)/2 minus actual sum  ->  O(n) time, O(1) space
  5. Bit manipulation: XOR all indices and values  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here