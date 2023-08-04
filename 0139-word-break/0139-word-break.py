class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possible = False
        @lru_cache(None)
        def go(string):
            nonlocal possible
            
            if possible:
                return
            
            for i in range(len(string)+1):
                #print(string[:i])
                if string[:i] in wordDict:
                    # print('0', i, len(string), string[:i])
                    if i == len(string):
                        possible = True
                        return
                    else:
                        #print('1', string[i:])
                        go(string[i:])
                        
        go(s)
        
        return possible