class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = []
        for i in range(R):
            for j in range(C):
                ans.append([abs(i-r0) + abs(j-c0), [i, j]])
                
        ans.sort()
        ans = [x[1] for x in ans]
        return ans