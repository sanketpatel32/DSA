"""
080_search_in_rotated_sorted_array

Question:
Search target in rotated sorted array without duplicates.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Approaches:
  1. Linear scan  ->  O(n) time, O(1) space
  2. Modified binary search locating the sorted half  ->  O(log n) time, O(1) space
  3. Find pivot first then binary search the right half  ->  O(log n) time, O(1) space
"""

# TODO: implement your solution here