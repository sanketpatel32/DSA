"""
144_task_scheduler

Question:
Min intervals to finish tasks with cooldown n.

Input: tasks=['A','A','A','B','B','B'], n=2
Output: 8

Approaches:
  1. Simulation with priority queue of counts  ->  O(time) time, O(n) space
  2. Math: most frequent task count formula  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here