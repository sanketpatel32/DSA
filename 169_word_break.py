"""
169_word_break

Question:
Return True if s can be segmented into dictionary words.

Input: s='leetcode', wordDict=['leet','code']
Output: True

Approaches:
  1. Recursion + memoization on suffix  ->  O(n^2 * m) time, O(n) space
  2. Bottom-up DP dp[i] = s[0..i] breakable  ->  O(n^2 * m) time, O(n) space
  3. BFS on indices  ->  O(n^2 * m) time, O(n) space
  4. Trie + DP  ->  O(n^2) time, O(n + trie size) space
"""

# TODO: implement your solution here