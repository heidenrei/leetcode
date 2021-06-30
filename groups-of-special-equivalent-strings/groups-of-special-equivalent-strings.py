class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        N = len(A)
        ans = 0
        used = set()
        
        for idx, w in enumerate(A):
            if idx not in used:
                ans += 1
                ce = Counter(w[::2])
                co = Counter(w[1::2])
                used.add(idx)
                for i in range(N):
                    if i not in used:
                        if Counter(A[i][::2]) == ce and Counter(A[i][1::2]) == co:
                            used.add(i)
                            
        return ans
                    
            
        