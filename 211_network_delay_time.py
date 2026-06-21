"""
211_network_delay_time

Question:
Time for signal from node k to reach all nodes.

Input: times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
Output: 2

Approaches:
  1. Dijkstra with min-heap  ->  O(E log V) time, O(V+E) space
  2. Bellman-Ford  ->  O(V*E) time, O(V) space
  3. SPFA (queue-based Bellman-Ford)  ->  O(V*E) avg time
"""

# TODO: implement your solution here