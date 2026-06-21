"""
001_palindrome_number
https://leetcode.com/problems/palindrome-number/description/
Question:
Given an integer x, return True if x is a palindrome, and False otherwise.

Input: x = 121
Output: True

Approaches:
  1. Convert to string and reverse-compare  ->  O(d) time, O(d) space  [d = number of digits]
  2. Two-pointer on string form (compare ends inward)  ->  O(d) time, O(d) space
  3. Revert half the integer mathematically (no string)  ->  O(log10 x) time, O(1) space
"""

# TODO: implement your solution here


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
