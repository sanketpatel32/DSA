"""
022_maximum_subarray

Question:
Find the contiguous subarray with the largest sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Approaches:
  1. Brute force: all subarrays  ->  O(n^2) (or O(n^3)) time, O(1) space
  2. Divide and conquer  ->  O(n log n) time, O(log n) space
  3. Kadane's algorithm (running sum)  ->  O(n) time, O(1) space
  4. Dynamic programming: dp[i] = max ending at i  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current subarray sum
        curr_sum = nums[0]

        # maximum sum found so far
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # either start new subarray from nums[i]
            # or continue previous subarray
            curr_sum = max(nums[i], curr_sum + nums[i])

            # update answer
            max_sum = max(max_sum, curr_sum)

        return max_sum