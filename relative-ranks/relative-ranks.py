class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        score = [[x, i] for i, x in enumerate(score)]
        score.sort(reverse=True)
        ranks = ["Bronze Medal","Silver Medal","Gold Medal"]
        
        ans = [0 for x in range(N)]
                
        for idx, x in enumerate(score[3:]):
            ans[x[1]] = str(idx+4)
            
        for x, i in score[:3]:
            ans[i] = ranks.pop()
            
        return ans