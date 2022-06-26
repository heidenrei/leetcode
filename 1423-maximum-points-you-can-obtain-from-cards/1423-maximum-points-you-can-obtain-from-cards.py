class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        rev = [cardPoints[-1-i] for i in range(k)]
        fw = [cardPoints[i] for i in range(k)]
        
        r_pfs = list(accumulate(rev))
        f_pfs = list(accumulate(fw))
        
        best = 0
        
        for i in range(k):
            tmp = r_pfs[i]
            if k - i  - 2 >= 0:
                tmp += f_pfs[k - i - 2]
                
            best = max(best, tmp)
            
            tmp = f_pfs[i]
            if k - i  - 2 >= 0:
                tmp += r_pfs[k - i - 2]
                
            best = max(best, tmp)
        
        return best