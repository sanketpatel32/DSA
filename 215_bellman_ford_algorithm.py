"""
215_bellman_ford_algorithm

Question:
Shortest paths allowing negative weights; detect negative cycles.

Input: graph with negative weights, source = 0
Output: distances or negative cycle

Approaches:
  1. Relax all edges V-1 times  ->  O(V*E) time, O(V) space
  2. One more pass to detect negative cycle  ->  O(E) time extra
  3. SPFA queue-based  ->  O(V*E) avg, O(V*E) worst time
"""

# TODO: implement your solution here