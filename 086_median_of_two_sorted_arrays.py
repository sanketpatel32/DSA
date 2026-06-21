"""
086_median_of_two_sorted_arrays

Question:
Find median of two sorted arrays in O(log(min(m,n))).

Input: nums1=[1,3], nums2=[2]
Output: 2.0

Approaches:
  1. Merge then pick median  ->  O(m+n) time, O(m+n) space
  2. Two-pointer merge without storing  ->  O(m+n) time, O(1) space
  3. Binary search on the smaller array's partition  ->  O(log(min(m,n))) time, O(1) space
"""

# TODO: implement your solution here