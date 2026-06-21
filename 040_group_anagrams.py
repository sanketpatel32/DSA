"""
040_group_anagrams

Question:
Group anagrams together from a list of strings.

Input: strs = ['eat','tea','tan','ate','nat','bat']
Output: grouped lists

Approaches:
  1. Sort each string as key in hash map  ->  O(n*k log k) time, O(n*k) space
  2. Character count tuple (size 26) as key  ->  O(n*k) time, O(n*k) space
  3. Prime-number product hash per string  ->  O(n*k) time, O(n*k) space
"""

# TODO: implement your solution here