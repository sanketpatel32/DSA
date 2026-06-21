"""
222_single_number

Question:
Every element twice except one; find it.

Input: nums = [4,1,2,1,2]
Output: 4

Approaches:
  1. Hash set: add/remove, leftover is answer  ->  O(n) time, O(n) space
  2. Sort and check adjacent pairs  ->  O(n log n) time, O(1) space
  3. XOR of all elements  ->  O(n) time, O(1) space
  4. Math: 2*sum(unique) - sum(all)  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here