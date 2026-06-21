"""
105_permutations

Question:
Return all permutations of a distinct-integer array.

Input: nums = [1,2,3]
Output: 6 permutations

Approaches:
  1. Backtracking with used-element set  ->  O(n*n!) time, O(n) space
  2. Backtracking with in-place swaps  ->  O(n*n!) time, O(1) extra space
  3. Iterative insertion (insert new element at every position)  ->  O(n*n!) time
  4. Heap's algorithm  ->  O(n*n!) time, O(1) extra space
"""

# TODO: implement your solution here