"""
044_two_sum_ii_input_array_is_sorted

Question:
1-indexed sorted array; return indices of two numbers summing to target.

Input: numbers=[2,7,11,15], target=9
Output: [1,2]

Approaches:
  1. Brute force pairs  ->  O(n^2) time, O(1) space
  2. Binary search for complement  ->  O(n log n) time, O(1) space
  3. Hash map of seen values  ->  O(n) time, O(n) space
  4. Two-pointer from both ends (optimal for sorted)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here