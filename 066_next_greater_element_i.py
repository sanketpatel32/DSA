"""
066_next_greater_element_i

Question:
For each nums1 element, find next greater in nums2.

Input: nums1=[4,1,2], nums2=[1,3,4,2]
Output: [-1,3,-1]

Approaches:
  1. Brute force: scan nums2 for each query  ->  O(n*m) time
  2. Monotonic decreasing stack to precompute NGE map  ->  O(n+m) time, O(n) space
"""

# TODO: implement your solution here