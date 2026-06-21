"""
171_partition_equal_subset_sum

Question:
Return True if array can split into two equal-sum subsets.

Input: nums = [1,5,11,5]
Output: True

Approaches:
  1. Recursion + memoization (subset sum = total/2)  ->  O(n*sum) time, O(n*sum) space
  2. Bottom-up DP (0/1 knapsack)  ->  O(n*sum) time, O(sum) space
  3. Bitset DP  ->  O(n*sum/word) time, O(sum) space
"""

# TODO: implement your solution here