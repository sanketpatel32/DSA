"""
011_reverse_string

Question:
Reverse a string (list of chars) in-place.

Input: s = ['h','e','l','l','o']
Output: ['o','l','l','e','h']

Approaches:
  1. Two-pointer swap from ends inward  ->  O(n) time, O(1) space
  2. Python slicing s[::-1] (new list)  ->  O(n) time, O(n) space
  3. Stack-based pop reversal  ->  O(n) time, O(n) space
  4. Recursion reversing first/last  ->  O(n) time, O(n) stack
"""

# TODO: implement your solution here

def swap(a:List)->List[char]:
    