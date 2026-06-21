"""
091_remove_nth_node_from_end_of_list

Question:
Remove the nth node from the end; return head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Approaches:
  1. Two passes: count then walk to (len-n)th  ->  O(n) time, O(1) space
  2. Two-pointer with n-gap (dummy head)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here