class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(' ')
        hash_map_1 = {}
        hash_map_2 = {}
        result = True
        if len(word_list) != len(pattern):
            result = False
        else:
            for idx, char in enumerate(pattern):
                word = word_list[idx]
                if (char in hash_map_1 and hash_map_1[char] != word) or (word in hash_map_2 and hash_map_2[word] != char):
                    result = False
                    break
                else:
                    hash_map_1[char] = word
                    hash_map_2[word] = char
        return result
