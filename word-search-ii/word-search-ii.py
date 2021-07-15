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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        words = list(set(words))
        
        DIRS = [[1,0], [0,1], [-1,0], [0,-1]]
        
        t = Trie()
        letter_set = set()
        for row in board:
            letter_set |= set(row)
        print(letter_set)
        tmp = []
        for word in words:
            if word[0] in letter_set:
                t.insert(word)
                tmp.append(word)
        
        words = tmp
        ans = set()
        
        def go(i, j, curr, used):
            if t.search(curr):
                ans.add(curr)
            for di, dj in DIRS:
                ni, nj = di + i, dj + j
                if 0 <= ni < R and 0 <= nj < C and t.startsWith(curr+board[ni][nj]) and tuple([ni, nj]) not in used:
                    tmp = list(used)
                    tmp.append(tuple([ni, nj]))
                    go(ni, nj, curr + board[ni][nj], tuple(tmp))
        
        print(words)
        
        for i in range(R):
            for j in range(C):
                if board[i][j] in t.root.edges and len(ans) < len(words):
                    tmp = [tuple([i, j])]
                    go(i, j, board[i][j], tuple(tmp))
                    
        return list(ans)
                    