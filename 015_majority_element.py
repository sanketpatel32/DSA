"""
015_majority_element
https://leetcode.com/problems/majority-element/

Question:
The majority element (>n/2 times). Return it.

Input: nums = [3,2,3]
Output: 3

Approaches:
  1. Brute force: count each element  ->  O(n^2) time, O(1) space
  2. Hash map frequency count  ->  O(n) time, O(n) space
  3. Sort and pick middle element  ->  O(n log n) time, O(1) (or O(n)) space
  4. Boyer-Moore majority vote  ->  O(n) time, O(1) space
  5. Divide and conquer  ->  O(n log n) time, O(log n) space
"""

# TODO: implement your solution here

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        ans=-1
        temp=len(nums)//2
        for i in dici:
            val=dici[i]
            if val > temp:
                ans=i
                break
        return ans
