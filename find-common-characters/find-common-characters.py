class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        N = len(A)
        
        ans = [x for x in A[0]]
        
        for i in range(1, N):
            tmp = [x for x in A[i]]
            j = 0
            while j < len(ans):
                if ans[j] in tmp:
                    tmp.pop(tmp.index(ans[j]))
                    j += 1
                else:
                    ans.pop(j)
        return ans
            
