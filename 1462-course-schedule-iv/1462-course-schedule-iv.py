class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(list)
        for x, y in p:
            d[y].append(x)
        print(d)
        pres = defaultdict(set)
        
        #@cache
        def go(node):
            ans = set()
            for nei in d[node]:
                if nei not in seen:
                    print(nei)
                    seen.add(nei)
                    ans.add(nei)
                    ans |= go(nei)
            return ans
        
        for x in range(n):
            seen = set([x])
            pres[x] = go(x)
        print(pres)
        ans = []
        for x, y in queries:
            ans.append(x in pres[y])
            
        return ans