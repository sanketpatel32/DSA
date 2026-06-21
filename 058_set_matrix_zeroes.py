"""
058_set_matrix_zeroes

Question:
If an element is 0, zero its entire row and column, in-place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: zeroed rows/cols

Approaches:
  1. Auxiliary row[] and col[] marker arrays  ->  O(m*n) time, O(m+n) space
  2. Use first row and first column as markers (in-place)  ->  O(m*n) time, O(1) space
  3. Use a single extra flag for first column  ->  O(m*n) time, O(1) space
"""

# TODO: implement your solution here