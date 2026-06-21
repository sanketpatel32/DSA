"""
235_count_of_smaller_numbers_after_self

Question:
For each element, count smaller elements to its right.

Input: nums = [5,2,6,1]
Output: [2,1,1,0]

Approaches:
  1. Brute force nested loops  ->  O(n^2) time, O(1) space
  2. Fenwick/BIT on coordinate-compressed values scanning right  ->  O(n log n) time, O(n) space
  3. Merge sort counting inversions per element  ->  O(n log n) time, O(n) space
  4. BST with subtree size (order statistic tree)  ->  O(n log n) avg, O(n) space
"""

# TODO: implement your solution here