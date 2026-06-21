"""
057_sliding_window_maximum

Question:
Max of each sliding window of size k.

Input: nums=[1,3,-1,-3,5,3,6,7], k=3
Output: [3,3,5,5,6,7]

Approaches:
  1. Brute force: max of each window  ->  O(n*k) time, O(1) space
  2. Monotonic deque storing useful candidates  ->  O(n) time, O(k) space
  3. Two bucketed max arrays (front/back blocks of size k)  ->  O(n) time, O(n) space
  4. Heap with lazy deletion (value,index)  ->  O(n log n) time, O(n) space
"""

# TODO: implement your solution here