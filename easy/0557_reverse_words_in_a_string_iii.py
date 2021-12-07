class Solution:
    def reverseWords(self, s: str) -> str:
        reversedWords = []
        for word in s.split(' '):
            reversedWords.append(word[::-1])
        return ' '.join(reversedWords)
