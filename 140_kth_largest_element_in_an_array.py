"""
140_kth_largest_element_in_an_array

Question:
Find the kth largest element.

Input: nums=[3,2,1,5,6,4], k=2
Output: 5

Approaches:
  1. Sort and pick index  ->  O(n log n) time, O(1) space
  2. Max-heap pop k times  ->  O(n + k log n) time, O(n) space
  3. Min-heap of size k  ->  O(n log k) time, O(k) space
  4. Quickselect (Hoare)  ->  O(n) avg, O(n^2) worst time, O(1) space
  5. Counting sort (small value range)  ->  O(n+V) time, O(V) space
"""

# TODO: implement your solution here