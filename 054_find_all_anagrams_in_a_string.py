"""
054_find_all_anagrams_in_a_string

Question:
Find all start indices in s that are anagrams of p.

Input: s='cbaebabacd', p='abc'
Output: [0,6]

Approaches:
  1. Sort p and compare each sorted window  ->  O(n * k log k) time
  2. Sliding window with frequency arrays  ->  O(n) time, O(1) space
  3. Sliding window with running match count  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here