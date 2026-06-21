"""
067_daily_temperatures

Question:
For each day, days until a warmer day (else 0).

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Approaches:
  1. Brute force nested loops  ->  O(n^2) time, O(1) space
  2. Monotonic decreasing stack of indices  ->  O(n) time, O(n) space
  3. Dynamic programming from right  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here