"""
098_lru_cache

Question:
LRU cache with get/put in O(1).

Input: capacity=2; put(1,1); put(2,2); get(1); put(3,3); get(2)
Output: 1, -1

Approaches:
  1. Hash map + doubly linked list  ->  O(1) get/put, O(capacity) space
  2. collections.OrderedDict  ->  O(1) get/put, O(capacity) space
  3. Hash map + counter-based recency (O(n) eviction)  ->  O(1) get/put avg, O(n) eviction
"""

# TODO: implement your solution here