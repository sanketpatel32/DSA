"""
157_gas_station

Question:
Return starting index to complete circuit, else -1.

Input: gas=[1,2,3,4,5], cost=[3,4,5,1,2]
Output: 3

Approaches:
  1. Brute force: try each start  ->  O(n^2) time, O(1) space
  2. Greedy one pass: if total surplus >=0, valid start after deficit gap  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here