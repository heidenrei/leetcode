class Node:
    def __init__(self):
        self.edges = {}
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        
        for ch in word:
            if ch not in curr.edges:
                curr.edges[ch] = Node()
                
            curr = curr.edges[ch]
                        
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        
        
        for ch in word:
            if ch not in curr.edges:
                return False
            
            curr = curr.edges[ch]
            
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        
        for ch in prefix:
            if ch not in curr.edges:
                return False
            curr = curr.edges[ch]
            
        return len(curr.edges) > 0 or curr.is_word
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)