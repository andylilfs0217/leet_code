from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return self.uniqueMorseRepresentations1(words)

    def uniqueMorseRepresentations1(self, words: List[str]) -> int:
        morse_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        res_set = set()
        for word in words:
            morse = ""
            for char in word:
                morse += morse_dict[char]
            res_set.add(morse)
        return len(res_set)
