"""
061_search_a_2d_matrix

Question:
Search target in matrix with sorted rows concatenated.

Input: matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3
Output: True

Approaches:
  1. Brute force scan  ->  O(m*n) time, O(1) space
  2. Binary search each row  ->  O(m log n) time, O(1) space
  3. Binary search treating matrix as one sorted array  ->  O(log(m*n)) time, O(1) space
  4. Two-pointer staircase (top-right corner)  ->  O(m+n) time, O(1) space
"""

# TODO: implement your solution here