"""
142_k_closest_points_to_origin

Question:
Return k closest points to origin.

Input: points=[[3,3],[5,-1],[-2,4]], k=2
Output: [[3,3],[-2,4]]

Approaches:
  1. Sort all by distance, take first k  ->  O(n log n) time, O(n) space
  2. Max-heap of size k  ->  O(n log k) time, O(k) space
  3. Quickselect to partition k closest  ->  O(n) avg time, O(1) space
  4. Min-heap pop k  ->  O(n + k log n) time, O(n) space
"""

# TODO: implement your solution here