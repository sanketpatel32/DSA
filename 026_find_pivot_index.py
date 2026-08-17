"""
026_find_pivot_index

Question:
Find index where left sum equals right sum.

Input: nums = [1,7,3,6,5,6]
Output: 3

Approaches:
  1. Brute force: recompute sums each index  ->  O(n^2) time, O(1) space
  2. Total sum minus prefix and current element  ->  O(n) time, O(1) space
  3. Prefix sum arrays  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here

def find_pivot_index(nums):
    sum = 0 
    for i in nums:
        sum += i
    pre_sum = 0
    for i in range(len(nums)):
        if sum - nums[i] == 2 * pre_sum :
            return i
        pre_sum += nums[i]

    return 0;

if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    print(find_pivot_index(nums))
            