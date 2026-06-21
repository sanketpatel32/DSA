"""
082_time_based_key_value_store

Question:
Set (key,value,timestamp); get returns most recent value <= timestamp.

Input: set('foo','bar',1), get('foo',1)
Output: 'bar'

Approaches:
  1. Dict of lists; linear scan on get  ->  O(1) set, O(n) get
  2. Dict of sorted lists; binary search on get  ->  O(1) set (append), O(log n) get
"""

# TODO: implement your solution here