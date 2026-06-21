"""
158_partition_labels

Question:
Partition string so each letter appears in only one part.

Input: s = 'ababcbacadefegdehijhklij'
Output: [9,7,8]

Approaches:
  1. Record last occurrence; extend current part to it  ->  O(n) time, O(1) space
  2. Merge intervals of first/last occurrence per letter  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here