"""
200_course_schedule

Question:
Return True if all courses can be finished (cycle detection).

Input: numCourses=2, prerequisites=[[1,0]]
Output: True

Approaches:
  1. DFS with three-color visited (cycle detection)  ->  O(V+E) time, O(V+E) space
  2. BFS Kahn's algorithm (in-degree)  ->  O(V+E) time, O(V+E) space
"""

# TODO: implement your solution here