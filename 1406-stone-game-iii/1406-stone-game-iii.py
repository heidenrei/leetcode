class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        N = len(stones)
        @cache
        def go(i, t):
            if i >= N:
                return 0
            if t:
                ans = -inf
                for di in range(1, 4):
                    if i + di > N:
                        break
                    #print(stones[i:i+di])
                    tmp = go(i+di, 1-t) + sum(stones[i:i+di])
                    if ans < tmp:
                        ans = tmp
                        
                return ans
            else:
                ans = inf
                for di in range(1,4):
                    if i + di > N:
                        break
                    #print(stones[i:i+di])
                    tmp = go(i+di, 1-t) - sum(stones[i:i+di])
                    if tmp < ans:
                        ans = tmp
                        
                return ans
            
        ans = go(0, 1)
        #print(ans)
        if ans == 0:
            return 'Tie'
        if ans > 0:
            return 'Alice'
        return 'Bob'
                    