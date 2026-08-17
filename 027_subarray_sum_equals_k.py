"""
027_subarray_sum_equals_k

Question:
Count continuous subarrays whose sum equals k.

Input: nums = [1,1,1], k = 2
Output: 2

Approaches:
  1. Brute force: all subarrays with running sum  ->  O(n^2) time, O(1) space
  2. Prefix sum + hash map of prefix frequencies  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        # prefix sum 0 occurs once (empty subarray before index 0)
        freq = {0: 1}

        for num in nums:
            prefix_sum += num
            # if (prefix_sum - k) seen before, those many subarrays end here with sum k
            count += freq.get(prefix_sum - k, 0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
