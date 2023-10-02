class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        bd = defaultdict(int)
        ad = defaultdict(int)
        N = len(colors)
        
        cnt = 0
        curr = None
        for i in range(N):
            if colors[i] == curr:
                cnt += 1
            else:
                if cnt >= 3:
                    if curr == 'A':
                        ad[cnt] += 1
                    else:
                        bd[cnt] += 1
                cnt = 1
                curr = colors[i]
                
        if cnt >= 3:
            if curr == 'A':
                ad[cnt] += 1
            else:
                bd[cnt] += 1
            
        anum = 0
        bnum = 0
        
        for k, v in ad.items():
            anum += (k - 2) * v
            
        for k, v in bd.items():
            bnum += (k - 2) * v
        
        #print(anum, bnum)
        
        return anum > bnum