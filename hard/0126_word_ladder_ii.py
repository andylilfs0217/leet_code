import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # return self.findLadders1(beginWord, endWord, wordList)
        return self.findLadders2(beginWord, endWord, wordList)

    # BFS. Time limit exceed. Time: O(n**n)
    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def findTwoStringDifference(s1: str, s2: str) -> int:
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            return count

        res = []
        if endWord not in wordList:
            return res
        minLen = 502
        # [curr_len, curr_list, curr_word_list]
        queue = [[1, [beginWord], wordList]]
        while queue:
            currLen, currList, currWordList = queue.pop(0)
            if currList[-1] == endWord and currLen <= minLen:
                res.append(currList)
                minLen = currLen
            elif currLen < minLen:
                for i, word in enumerate(currWordList):
                    if findTwoStringDifference(currList[-1], word) == 1:
                        queue.append([currLen+1, currList+[word],
                                      currWordList[:i]+currWordList[i+1:]])
        return res

    # BFS
    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord or not beginWord or not wordList or endWord not in wordList \
                or beginWord == endWord:
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Shortest path, BFS
        ans = []
        queue = collections.deque()
        queue.append((beginWord, [beginWord]))
        visited = set([beginWord])

        while queue and not ans:
            # print(queue)
            length = len(queue)
            # print(queue)
            localVisited = set()
            for _ in range(length):
                word, path = queue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == endWord:
                            # path.append(endword)
                            ans.append(path+[endWord])
                        if nextWord not in visited:
                            localVisited.add(nextWord)
                            queue.append((nextWord, path+[nextWord]))
            visited = visited.union(localVisited)
        return ans
