"""
236_reverse_pairs

Question:
Count pairs i<j where nums[i] > 2*nums[j].

Input: nums = [1,3,2,3,1]
Output: 2

Approaches:
  1. Brute force nested loops  ->  O(n^2) time, O(1) space
  2. Merge sort counting cross-pairs during merge  ->  O(n log n) time, O(n) space
  3. Fenwick/BIT on coordinate-compressed 2*x values  ->  O(n log n) time, O(n) space
  4. BST with augmented counts  ->  O(n log n) avg, O(n) space
"""

# TODO: implement your solution here