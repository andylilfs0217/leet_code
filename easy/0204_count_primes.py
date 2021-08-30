class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        isPrime = [1] * (n + 1)
        isPrime[0] = isPrime[1] = 0
        ans = 0
        for i in range(2, n + 1):
            if isPrime[i] == 1:
                ans += 1
                for j in range(i*2, n + 1, i):
                    isPrime[j] = 0

        return ans


Solution().countPrimes(10)
