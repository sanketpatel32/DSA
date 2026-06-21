"""
017_move_zeroes

Question:
Move all 0's to the end in-place preserving order of non-zeros.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Approaches:
  1. Auxiliary array of non-zeros then pad zeros  ->  O(n) time, O(n) space
  2. Two-pointer: slow for insert position, fast for scan  ->  O(n) time, O(1) space
  3. Snowball: swap accumulating zero block with next non-zero  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here