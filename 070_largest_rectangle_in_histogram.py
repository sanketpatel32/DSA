"""
070_largest_rectangle_in_histogram

Question:
Area of largest rectangle in a histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10

Approaches:
  1. Brute force: for each bar expand outward  ->  O(n^2) time, O(1) space
  2. Monotonic stack of indices  ->  O(n) time, O(n) space
  3. Precompute left/right smaller arrays then single pass  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here