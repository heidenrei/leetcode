class Node:
    def __init__(self):
        self.edges = {}
        self.words = []
        
    def add_word(self, word):
        self.words.append(word)
        self.words.sort()
        
        if len(self.words) > 3:
            self.words.pop()
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        curr = self.root
                
        for ch in word:
            if ch not in curr.edges:
                curr.edges[ch] = Node()
            
            curr.add_word(word)
            curr = curr.edges[ch]
            
        curr.add_word(word)
        
    def search(self, word):
        ans = []
        curr = self.root
        
        for ch in word:
            if ch not in curr.edges:
                ans.append([])
                break
                
            curr = curr.edges[ch]
            ans.append(curr.words)
            
        while len(ans) < len(word):
            ans.append([])
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        #products.sort(reverse=True)
        for p in products:
            t.add(p)
        
        return t.search(searchWord)