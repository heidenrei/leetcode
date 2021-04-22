class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        R, C = len(wall), len(wall[0])
        
        A = []
        d = defaultdict(int)
        for i in range(R):
            A.append(list(accumulate(wall[i])))
            
        for i in range(R):
            for j in range(len(A[i])-1):
                d[A[i][j]] += 1
                
        return R - max(d.values()) if d.values() else R