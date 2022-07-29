from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # return self.findAndReplacePattern1(words, pattern)
        return self.findAndReplacePattern2(words, pattern)

    def findAndReplacePattern1(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            p2w, w2p = {}, {}
            same_pattern = True
            i = 0
            while same_pattern and i < len(word):
                char_in_word, char_in_pattern = word[i], pattern[i]
                should_char_in_word, should_char_in_pattern = p2w.get(
                    char_in_pattern, None), w2p.get(char_in_word, None)
                if not should_char_in_word and not should_char_in_pattern:
                    p2w[char_in_pattern] = char_in_word
                    w2p[char_in_word] = char_in_pattern
                elif char_in_pattern != should_char_in_pattern or char_in_word != should_char_in_word:
                    same_pattern = False
                i += 1
            if same_pattern:
                result.append(word)
        return result

    def findAndReplacePattern2(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)


print(Solution().findAndReplacePattern(words=[
      "abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb") == ["mee", "aqq"])
print(Solution().findAndReplacePattern(
    words=["a", "b", "c"], pattern="a") == ["a", "b", "c"])
