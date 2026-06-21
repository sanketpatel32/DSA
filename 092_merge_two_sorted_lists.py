"""
092_merge_two_sorted_lists

Question:
Merge two sorted linked lists; return head.

Input: list1=[1,2,4], list2=[1,3,4]
Output: [1,1,2,3,4,4]

Approaches:
  1. Iterative dummy head with compare-and-attach  ->  O(n+m) time, O(1) space
  2. Recursive merge  ->  O(n+m) time, O(n+m) stack
"""

# TODO: implement your solution here