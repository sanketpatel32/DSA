"""
005_excel_sheet_column_number
https://leetcode.com/problems/excel-sheet-column-number/description/
Question:
Given an Excel column title, return its column number.

Input: columnTitle = 'AB'
Output: 28

Approaches:
  1. Left-to-right Horner-style accumulation: res = res*26 + digit  ->  O(n) time, O(1) space
"""


# TODO: implement your solution here
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord("A") + 1)
        return ans
