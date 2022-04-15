from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        modified = list(s)
        for index, source, target in zip(indices, sources, targets):
            if not s[index:].startswith(source):
                continue
            else:
                modified[index] = target
                for i in range(index+1, len(source)+index):
                    modified[i] = ""
        return "".join(modified)


print(Solution().findReplaceString("vmokgggqzp",
                                   [3, 5, 1],
                                   ["kg", "ggq", "mo"],
                                   ["s", "so", "bfr"]))
