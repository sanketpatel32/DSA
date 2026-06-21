"""
030_top_k_frequent_elements

Question:
Return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approaches:
  1. Hash map + sort by frequency  ->  O(n log n) time, O(n) space
  2. Hash map + min-heap of size k  ->  O(n log k) time, O(n) space
  3. Bucket sort by frequency (freq buckets)  ->  O(n) time, O(n) space
  4. Quickselect on frequencies  ->  O(n) avg time, O(n) space
"""

# TODO: implement your solution here