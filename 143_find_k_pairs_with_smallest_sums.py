"""
143_find_k_pairs_with_smallest_sums

Question:
Find k pairs (one from each array) with smallest sums.

Input: nums1=[1,7,11], nums2=[2,4,6], k=3
Output: pairs

Approaches:
  1. Generate all pairs, sort, take k  ->  O(n*m log(n*m)) time
  2. Min-heap with index pairs, push successors lazily  ->  O(k log k) time, O(k) space
"""

# TODO: implement your solution here