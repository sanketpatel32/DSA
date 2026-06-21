"""
074_number_of_recent_calls

Question:
Count pings in the last 3000ms.

Input: ping(1), ping(100), ping(3001), ping(3002)
Output: 1,2,3,3

Approaches:
  1. List with binary search for window start  ->  O(log n) per ping, O(n) space
  2. FIFO queue evicting out-of-window pings  ->  O(1) amortized per ping, O(n) space
"""

# TODO: implement your solution here