"""
041_ransom_note

Question:
Return True if ransomNote can be built from magazine letters.

Input: ransomNote='aa', magazine='aab'
Output: True

Approaches:
  1. Sort both and compare counts  ->  O(m log m + n log n) time
  2. Frequency array (26) of magazine, decrement for note  ->  O(m+n) time, O(1) space
  3. collections.Counter subtraction  ->  O(m+n) time, O(1) space
"""

# TODO: implement your solution here