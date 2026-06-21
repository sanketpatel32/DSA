"""
159_hand_of_straights

Question:
Return True if cards can be grouped into consecutive groupSize runs.

Input: hand=[1,2,3,6,2,3,4,7,8], groupSize=3
Output: True

Approaches:
  1. Sort + frequency map; greedily form groups from smallest  ->  O(n log n) time, O(n) space
  2. Ordered map / TreeMap of counts  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here