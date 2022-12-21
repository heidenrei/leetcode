class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        s = defaultdict(int)
        d = defaultdict(list)
        for x, y in dislikes:
            d[x].append(y)
            d[y].append(x)
            
        def go(x):
            for y in d[x]:
                if y in s and s[y] == s[x]:
                    return False
                if y not in s:
                    s[y] = 1-s[x]
                    if not go(y):
                        return False
                
            return True
        
        for x in range(1, n+1):
            if x not in s:
                s[x] = 0
                if not go(x):
                    return False
                
        return True