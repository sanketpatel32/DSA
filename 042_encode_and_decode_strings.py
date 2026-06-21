"""
042_encode_and_decode_strings

Question:
Encode a list of strings into one and decode it back losslessly.

Input: ['Hello','World']
Output: round-trips to ['Hello','World']

Approaches:
  1. Length-prefixed encoding ('len#str' format)  ->  O(n) time, O(n) space
  2. Escape delimiter strategy  ->  O(n) time, O(n) space
  3. Chunked transfer style with fixed-width length header  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here