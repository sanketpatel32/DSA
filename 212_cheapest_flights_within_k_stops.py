"""
212_cheapest_flights_within_k_stops

Question:
Cheapest price from src to dst with at most k stops.

Input: n=4, flights=[...], src=0, dst=3, k=1
Output: 700

Approaches:
  1. Bellman-Ford limited to k+1 iterations  ->  O(k*E) time, O(V) space
  2. BFS level by level (k+1 levels)  ->  O(k*E) time, O(V) space
  3. Dijkstra variant tracking stops (state = (node,stops))  ->  O(V*E) time, O(V) space
"""

# TODO: implement your solution here