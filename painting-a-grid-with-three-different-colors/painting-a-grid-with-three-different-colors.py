class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9+7
        all_ones = [[x+1] for x in range(3)]
        for _ in range(1, m):
            tmp = []
            for x in range(1, 4):
                for i in range(len(all_ones)):
                    if all_ones[i][-1] != x:
                        tmp.append(all_ones[i] + [x])
                    
            all_ones = tmp
        
        all_ones = [tuple(x) for x in all_ones]
        
        d = defaultdict(list)
        
        def go(prev):
            for arr in all_ones:
                possible = True
                for idx in range(m):
                    if prev[idx] == arr[idx]:
                        possible = False
                        break
                if possible:
                    d[prev].append(arr)
                
        for i in range(len(all_ones)):
            go(tuple(all_ones[i]))
            
        dp = Counter(all_ones)
        for _ in range(n-1):
            dp2 = Counter()
            for c1 in all_ones:
                for c2 in d[c1]:
                    dp2[c2] = (dp2[c2] + dp[c1]) % MOD
            dp = dp2

        return sum(dp.values()) % MOD
        