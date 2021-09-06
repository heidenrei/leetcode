class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = defaultdict(int)
        d[keysPressed[0]] = releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            d[keysPressed[i]] = max(d[keysPressed[i]], releaseTimes[i] - releaseTimes[i-1])
            
        maxi = max([x for x in d.values()])
        ans = None
        for k, v in d.items():
            if v == maxi:
                if ans:
                    ans = max(k, ans)
                else:
                    ans = k
                    
        return ans