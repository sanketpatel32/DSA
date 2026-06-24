"""
006_count_primes
https://leetcode.com/problems/count-primes/description/

Question:
Return the number of prime numbers strictly less than n.

Input: n = 10
Output: 4

Approaches:
  1. Trial division per number  ->  O(n*sqrt(n)) time, O(1) space
  2. Sieve of Eratosthenes  ->  O(n log log n) time, O(n) space
"""

# TODO: implement your solution here

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2,int(n**0.5 +1)):
            if is_prime[i]:
                for j in range(i+i,n,i):
                    is_prime[j] = False
        return sum(is_prime)