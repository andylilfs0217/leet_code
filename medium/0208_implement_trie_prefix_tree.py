class Trie:

    def __init__(self):
        self.trie_list: set = set()
        self.start_list: dict = {}

    def insert(self, word: str) -> None:
        self.trie_list.add(word)
        curr_char_dict = self.start_list
        for char in word:
            if curr_char_dict.get(char) is None:
                curr_char_dict[char] = {}
            curr_char_dict = curr_char_dict[char]

    def search(self, word: str) -> bool:
        return word in self.trie_list

    def startsWith(self, prefix: str) -> bool:
        curr_char_dict = self.start_list
        for char in prefix:
            if curr_char_dict.get(char) is None:
                return False
            curr_char_dict = curr_char_dict[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
