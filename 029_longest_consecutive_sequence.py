"""
029_longest_consecutive_sequence

Question:
Length of longest consecutive elements sequence in O(n).

Input: nums = [100,4,200,1,3,2]
Output: 4

Approaches:
  1. Sort then scan for consecutive runs  ->  O(n log n) time, O(1) (or O(n)) space
  2. Hash set; only expand from sequence starts  ->  O(n) time, O(n) space
  3. Union-Find on consecutive values  ->  O(n) time (amortized), O(n) space
"""

# TODO: implement your solution here