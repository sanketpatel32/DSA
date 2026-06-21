"""
230_maximum_xor_of_two_numbers_in_an_array

Question:
Maximum result of nums[i] XOR nums[j].

Input: nums = [3,10,5,25,2,8]
Output: 28

Approaches:
  1. Brute force all pairs  ->  O(n^2) time, O(1) space
  2. Trie of binary prefixes; for each num find max XOR partner  ->  O(n * B) time, O(n * B) space  (B = bits)
  3. Hash set + greedy prefix building  ->  O(n * B) time, O(n) space
"""

# TODO: implement your solution here