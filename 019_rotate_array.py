"""
019_rotate_array

Question:
Rotate the array to the right by k steps in-place.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Approaches:
  1. Extra array: place each element at (i+k)%n  ->  O(n) time, O(n) space
  2. Reverse whole, then reverse first k and rest  ->  O(n) time, O(1) space
  3. Cyclic replacements (jump by k mod n)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
    
    