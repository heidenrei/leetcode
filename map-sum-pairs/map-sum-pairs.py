class Node:
    def __init__(self):
        self.children = {}
        self.val_sum = 0

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word, new_val, old_val):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.val_sum += new_val - old_val
        
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return 0
        return curr.val_sum

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()
        self.d = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        old_val = self.d[key]
        self.t.insert(key, val, old_val)
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        return self.t.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)