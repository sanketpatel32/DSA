"""
094_reorder_list

Question:
Reorder as L0->Ln->L1->Ln-1->... in-place.

Input: 1->2->3->4
Output: 1->4->2->3

Approaches:
  1. Store nodes in array then reconnect  ->  O(n) time, O(n) space
  2. Find middle, reverse second half, interleave  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here