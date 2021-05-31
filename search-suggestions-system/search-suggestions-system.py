class Node:
    def __init__(self):
        self.edges = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = Node()
        
    def add_word(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.edges:
                curr.edges[ch] = Node()
            curr = curr.edges[ch]
            curr.words.append(word)
            
            if len(curr.words) > 3:
                curr.words.pop()
                
    def search(self, prefix):
        curr = self.root
        
        for ch in prefix:
            if ch not in curr.edges:
                return ''
            curr = curr.edges[ch]
            
        return curr.words
            
                
            
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        
        t = Trie()
        
        for p in products:
            t.add_word(p)
            
        ans = []
        curr = ''
            
        for ch in searchWord:
            curr += ch
            ans.append(t.search(curr))
            
        return ans