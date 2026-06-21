"""
024_product_of_array_except_self

Question:
output[i] = product of all except nums[i], without division, in O(n).

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Approaches:
  1. Division: total product / nums[i] (handle zeros)  ->  O(n) time, O(1) extra space
  2. Left and right prefix product arrays  ->  O(n) time, O(n) space
  3. Single output array with running prefix (left then right sweep)  ->  O(n) time, O(1) extra space
"""

# TODO: implement your solution here