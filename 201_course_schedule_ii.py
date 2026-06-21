"""
201_course_schedule_ii

Question:
Return a valid course order (topological sort).

Input: numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]

Approaches:
  1. DFS post-order reversed  ->  O(V+E) time, O(V+E) space
  2. BFS Kahn's algorithm (in-degree queue)  ->  O(V+E) time, O(V+E) space
"""

# TODO: implement your solution here