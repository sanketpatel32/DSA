"""
224_counting_bits

Question:
ans[i] = popcount of i for i in 0..n.

Input: n = 5
Output: [0,1,1,2,1,2]

Approaches:
  1. Compute popcount for each number independently  ->  O(n log n) time, O(n) space
  2. DP: ans[i] = ans[i >> 1] + (i & 1)  ->  O(n) time, O(n) space
  3. DP: ans[i] = ans[i & (i-1)] + 1  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here