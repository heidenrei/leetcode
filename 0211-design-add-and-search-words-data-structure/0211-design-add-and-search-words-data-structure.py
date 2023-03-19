class Node:
    __slots__ = 'val', 'children', 'is_word'
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = Node(x)
            curr = curr.children[x]
        curr.is_word = True
        
    #@cache
    def search(self, curr, word, i):
        if i == len(word):
            return curr.is_word
        if word[i] in curr.children and self.search(curr.children[word[i]], word, i+1):
            return True
        if word[i] == '.':
            for child in curr.children:
                if self.search(curr.children[child], word, i+1):
                    return True
        return False
        
class WordDictionary:

    def __init__(self):
        self.t = Trie()

    def addWord(self, word: str) -> None:
        self.t.add(word)

    def search(self, word: str) -> bool:
        return self.t.search(self.t.root, word, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)