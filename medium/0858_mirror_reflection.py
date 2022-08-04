class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        return self.mirrorReflection1(p, q)

    def mirrorReflection1(self, p: int, q: int) -> int:
        i = 1
        while i <= p and i <= q:
            if p % i == 0 and q % i == 0:
                gcd = i
            i += 1
        lcm = (p*q)//gcd

        res = -1
        temp = lcm // p
        if temp % 2 == 1 and (lcm//q) % 2 == 0:
            res = 2
        elif temp % 2 == 1 and (lcm//q) % 2 == 1:
            res = 1
        elif temp % 2 == 0 and (lcm//q) % 2 == 1:
            res = 0
        return res


print(Solution().mirrorReflection(2, 1) == 2)
print(Solution().mirrorReflection(3, 1) == 1)
print(Solution().mirrorReflection(3, 2) == 0)
