"""
003_add_binary

Question:
Given two binary strings a and b, return their sum as a binary string.

Input: a = '11', b = '1'
Output: '100'

Approaches:
  1. Bit-by-bit simulation from right with carry  ->  O(max(n,m)) time, O(max(n,m)) space
  2. Convert to int, sum, format back to binary (Python int(a,2))  ->  O(max(n,m)) time, O(max(n,m)) space  (limited by int width)
  3. Bit manipulation without full string conversion  ->  O(max(n,m)) time, O(max(n,m)) space
"""


# TODO: implement your solution here
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry = carry // 2
        return "".join(reversed(s))
