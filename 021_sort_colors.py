"""
021_sort_colors

Question:
Sort an array of only 0,1,2 in-place (Dutch National Flag).

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Approaches:
  1. Counting sort: count 0s/1s/2s then rewrite  ->  O(n) time, O(1) space (two passes)
  2. Dutch National Flag three-pointer (low/mid/high)  ->  O(n) time, O(1) space (one pass)
  3. General comparison sort  ->  O(n log n) time, O(1) space
"""


# TODO: implement your solution here
def sort_colors(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid < high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            mid += 1
            high -= 1
