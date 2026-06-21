"""
005_excel_sheet_column_number

Question:
Given an Excel column title, return its column number.

Input: columnTitle = 'AB'
Output: 28

Approaches:
  1. Left-to-right Horner-style accumulation: res = res*26 + digit  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here