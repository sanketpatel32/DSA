"""
096_merge_k_sorted_lists

Question:
Merge k sorted linked lists into one.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: merged

Approaches:
  1. Collect all values, sort, rebuild  ->  O(N log N) time, O(N) space
  2. Pairwise merge lists  ->  O(N log k) time, O(1) space
  3. Min-heap of current heads  ->  O(N log k) time, O(k) space
  4. Divide and conquer merging  ->  O(N log k) time, O(log k) stack
"""

# TODO: implement your solution here