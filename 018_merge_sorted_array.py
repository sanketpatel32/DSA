"""
018_merge_sorted_array

Question:
Merge nums1 (m elements) and nums2 (n elements) in-place into nums1.

Input: nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
Output: [1,2,2,3,5,6]

Approaches:
  1. Copy nums2 in, then sort nums1  ->  O((m+n) log(m+n)) time, O(1) space
  2. Three pointers from the end (fill largest first)  ->  O(m+n) time, O(1) space
  3. Auxiliary array merge from front  ->  O(m+n) time, O(m+n) space
"""

# TODO: implement your solution here