"""
060_rotate_image

Question:
Rotate an n x n matrix 90 degrees clockwise in-place.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: rotated

Approaches:
  1. Auxiliary matrix copy  ->  O(n^2) time, O(n^2) space
  2. Transpose then reverse each row  ->  O(n^2) time, O(1) space
  3. Rotate four cells in place layer by layer  ->  O(n^2) time, O(1) space
"""

# TODO: implement your solution here