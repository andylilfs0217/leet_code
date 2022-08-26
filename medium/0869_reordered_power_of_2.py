from collections import Counter


class Solution:
    MAX_N = 10**9

    def reorderedPowerOf2(self, n: int) -> bool:
        # return self.reorderedPowerOf21(n)
        return self.reorderedPowerOf22(n)

    def reorderedPowerOf21(self, n: int) -> bool:
        po2s = set()
        i = 1
        while i <= self.MAX_N:
            tmp = ''.join(sorted(str(i)))
            po2s.add(tmp)
            i = i << 1

        nStr = ''.join(sorted(str(n)))
        if nStr in po2s:
            return True
        return False

    def reorderedPowerOf22(self, n: int) -> bool:
        i = 1
        nCounter = Counter(str(n))
        while i <= self.MAX_N:
            iCounter = Counter(str(i))
            if nCounter == iCounter:
                return True
            i = i << 1
        return False


print(Solution().reorderedPowerOf2(1) == True)
print(Solution().reorderedPowerOf2(10) == False)
print(Solution().reorderedPowerOf2(23) == True)
