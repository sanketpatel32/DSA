"""
002_plus_one
https://leetcode.com/problems/plus-one/
Question:
Given a large integer as a digit array, increment it by one and return the result.

Input: digits = [1,2,3]
Output: [1,2,4]

Approaches:
  1. Schoolbook addition from the last digit with carry  ->  O(n) time, O(1) space (in-place; O(n) only on all-9 overflow)
"""

# TODO: implement your solution here
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1 
        
        for i in range(len(digits) - 1, -1, -1):
            n = digits[i] + carry
            carry = 1 if n >= 10 else 0
            digits[i] = n % 10 
            
        if carry:
            return [1] + digits
        else:
            return digits