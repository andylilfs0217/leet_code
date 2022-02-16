from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        count = 0
        for i in range(2, int(sqrt(n))+1):
            if isPrime[i]:
                for j in range(i**2, n, i):
                    isPrime[j] = False
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
