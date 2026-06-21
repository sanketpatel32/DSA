"""
207_accounts_merge

Question:
Merge accounts sharing any email.

Input: accounts=[...]
Output: merged accounts

Approaches:
  1. Union-Find on email addresses  ->  O(n*k * a) time, O(n*k) space
  2. DFS on email adjacency graph  ->  O(n*k) time, O(n*k) space
  3. BFS connected components  ->  O(n*k) time, O(n*k) space
"""

# TODO: implement your solution here