class Solution:
    def checkPartitioning(self, s: str) -> bool:
        N = len(s)
        odds = defaultdict(list)
        evens = defaultdict(list)
        for i in range(N):
            odds[i] = [i, i]
            evens[i] = [i, i]
            idx = 1
            while (0 <= i-idx and idx+i < N) and s[i-idx] == s[i+idx]:
                odds[i] = [min(odds[i][0], i-idx), max(odds[i][1], i+idx)]
                idx += 1
            idx = 1
            while (0 <= i-idx+1 and idx+i < N) and s[i-idx+1] == s[i+idx]:
                evens[i] = [min(evens[i][0], i-idx+1), max(evens[i][1], i+idx)]
                idx += 1
        
        combos = set()
        
        for x, y in odds.values():
            combos.add(tuple([x, y]))
        
        for x, y in evens.values():
            combos.add(tuple([x, y]))
        
        for i in range(N):
            combos.add(tuple([i, i]))
        
        starts = []
        ends = []
        for i in range(N-2):
            if odds[i][0] == 0:
                starts.append(odds[i][1]+1)
                
            if evens[i][0] == 0:
                starts.append(evens[i][1]+1)
                
        for i in range(2, N):
            if odds[i][1] == N-1:
                ends.append(odds[i][0]-1)
            if evens[i][1] == N-1:
                ends.append(evens[i][0]-1)
        
        starts = set(starts)
        ends = set(ends)
        
#         print(combos)
#         print(starts)
#         print(ends)
        
        
        for s in starts:
            for e in ends:
                if tuple([s, e]) in combos:
                    return True
                
        return False
        
