"""
075_design_hit_counter

Question:
Count hits in the past 5 minutes.

Input: hit(1), hit(2), hit(3), getHits(4), getHits(300), getHits(301)
Output: 3,2,2

Approaches:
  1. List of timestamps, evict older on getHits  ->  O(n) getHits, O(n) space
  2. Deque with eviction of out-of-window hits  ->  O(1) amortized getHits, O(n) space
  3. Bucketed counters per second (size 300)  ->  O(1) hit and getHits, O(1) space
"""

# TODO: implement your solution here