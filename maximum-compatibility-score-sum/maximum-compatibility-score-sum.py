class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        N = len(students)
        
        @lru_cache(None)
        def go(sbm, mbm):
            if sbm == 2**N-1:
                return 0
            
            best = 0
            
            for i in range(N):
                for j in range(N):
                    if not sbm & (1<<i) and not mbm & (1<<j):
                        tmp = 0
                        for k in range(len(students[0])):
                            tmp += students[i][k] == mentors[j][k]
                        best = max(best, go(sbm | (1<<i), mbm | (1<<j)) + tmp)
                                   
            return best
                                   
        return go(0, 0)