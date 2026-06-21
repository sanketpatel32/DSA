"""
025_range_sum_query_immutable

Question:
Answer many range sum [left,right] queries using a prefix sum.

Input: nums=[-2,0,3,-5,2,-1], query=[0,2]
Output: 1

Approaches:
  1. Naive: sum the range each query  ->  O(1) preprocess, O(n) per query
  2. Prefix sum array: P[right+1]-P[left]  ->  O(n) preprocess, O(1) per query
"""

# TODO: implement your solution here