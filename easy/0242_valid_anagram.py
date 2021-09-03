class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1

        for val in dic.values():
            if val != 0:
                return False

        return True
