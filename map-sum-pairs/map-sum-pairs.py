class Node:
    def __init__(self):
        self.val = 0
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = Node()
        self.d = defaultdict(int)
        
    def insert(self, val, key):
        curr = self.root
        
        for ch in key:
            if ch not in curr.children:
                curr.children[ch] = Node()
                
            curr = curr.children[ch]
            curr.val += val
            curr.val -= self.d[key]
            
        self.d[key] = val
            
    def query(self, prefix):
        curr = self.root
        
        for ch in prefix:
            if ch not in curr.children:
                return 0
            else:
                curr = curr.children[ch]
                
        return curr.val

class MapSum:
    def __init__(self):
        self.t = Trie()

    def insert(self, key: str, val: int) -> None:
        self.t.insert(val, key)

    def sum(self, prefix: str) -> int:
        return self.t.query(prefix)