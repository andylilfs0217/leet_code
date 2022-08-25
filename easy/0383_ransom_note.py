from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return self.canConstruct1(ransomNote, magazine)

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        for char, count in ransomNoteCount.items():
            if count > magazineCount.get(char, 0):
                return False
        return True


print(Solution().canConstruct(ransomNote="a", magazine="b") == False)
print(Solution().canConstruct(ransomNote="aa", magazine="ab") == False)
print(Solution().canConstruct(ransomNote="aa", magazine="aab") == True)
