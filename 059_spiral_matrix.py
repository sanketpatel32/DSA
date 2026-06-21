"""
059_spiral_matrix

Question:
Return all elements of an m x n matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Approaches:
  1. Layer-by-layer with four boundaries (top/bottom/left/right)  ->  O(m*n) time, O(1) extra space
  2. Direction vector switching on boundary/visited  ->  O(m*n) time, O(m*n) space (visited set)
"""

# TODO: implement your solution here