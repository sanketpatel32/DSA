"""
048_trapping_rain_water

Question:
Compute total trapped rainwater between bars.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Approaches:
  1. Brute force: for each bar, scan for left/right max  ->  O(n^2) time, O(1) space
  2. Prefix max arrays (left[] and right[])  ->  O(n) time, O(n) space
  3. Two-pointer from both ends  ->  O(n) time, O(1) space
  4. Monotonic decreasing stack  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here