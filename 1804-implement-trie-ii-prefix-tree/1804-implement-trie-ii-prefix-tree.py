class Node:
    __slots__ = 'value', 'cnt', 'children', 'is_word'
    def __init__(self, value):
        self.value = value
        self.cnt = 0
        self.children = {}
        self.is_word = 0

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = Node(x)
            curr = curr.children[x]
            curr.cnt += 1
        curr.is_word += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for x in word:
            if x not in curr.children:
                return 0
            else:
                curr = curr.children[x]
        return curr.is_word

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for x in prefix:
            if x not in curr.children:
                return 0
            else:
                curr = curr.children[x]
        return curr.cnt

    def erase(self, word: str) -> None:
        curr = self.root
        for x in word:
            curr = curr.children[x]
            curr.cnt -= 1
        curr.is_word -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)