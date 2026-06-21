"""
037_longest_common_prefix

Question:
Find longest common prefix among an array of strings.

Input: strs = ['flower','flow','flight']
Output: 'fl'

Approaches:
  1. Horizontal scanning: prefix vs each string  ->  O(S) time, O(1) space
  2. Vertical scanning: char-by-char across strings  ->  O(S) time, O(1) space
  3. Divide and conquer  ->  O(S) time, O(m log n) space
  4. Sort and compare first vs last string  ->  O(n log n * L) time, O(1) space
  5. Trie of all strings then walk common branch  ->  O(S) time, O(S) space
"""

# TODO: implement your solution here