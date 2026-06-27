"""
020_remove_duplicates_from_sorted_array

Question:
Remove duplicates in-place from a sorted array; return new length.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Approaches:
  1. Two-pointer: slow for unique slot, fast for scan  ->  O(n) time, O(1) space
  2. Hash set then overwrite (works but loses O(1) space)  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[j] = nums[i]
                j += 1
        return j