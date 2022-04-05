class Node:
    def __init__(self):
        self.edges = {}
        self.is_word = False

class Trie:
    def __init__(self, keys, values, dictionary):
        self.root = Node()
        self.keys = keys
        self.values = values
        self.dictionary = dictionary
        self.en = defaultdict(list)
        self.de = defaultdict(list)

        for i in range(len(keys)):
            self.en[keys[i]].append(values[i])
            self.de[values[i]].append(keys[i])
    def insert(self, word: str) -> None:
        curr = self.root
        
        for ch in word:
            if ch not in curr.edges:
                curr.edges[ch] = Node()
                
            curr = curr.edges[ch]
                        
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        def go(curr, word):
            if not word and curr.is_word:
                return 1
            
            ans = 0
            if word[:2] in self.de:
                for v in self.de[word[:2]]:
                    #print(v)
                    if v in curr.edges:
                        #print(v)
                        ans += go(curr.edges[v], word[2:])
            return ans
        
        return go(curr, word)

class Encrypter:
    # check if we can do any of the strings in dictionary
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.allowed = set(dictionary)
        self.t = Trie(keys, values, dictionary)
        for x in dictionary:
            self.t.insert(x)
        self.en = defaultdict(list)
        self.de = defaultdict(list)

        for i in range(len(keys)):
            self.en[keys[i]].append(values[i])
            self.de[values[i]].append(keys[i])
        

    def encrypt(self, word1: str) -> str:
        ans = ''
        for x in word1:
            ans += self.en[x][0]
            
        return ans

    def decrypt(self, word2: str) -> int:
        return self.t.search(word2)