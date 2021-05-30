class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        
        def go(x):
            if len(x) == n:
                ans.append(x)
                return
                
            last = int(x[-1])
                
            if last + k <= 9:
                go(x + str(last + k))
                
            if last - k >= 0:
                go(x + str(last - k))
                
        for x in range(1, 10):
            go(str(x))
            
        return list(set(ans))