from sortedcontainers import SortedList
​
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        N = len(instructions)
        MOD = 10**9+7
        cnt = 0
        A = SortedList()
        
        for i in range(N):
            left = A.bisect_left(instructions[i])
            right = A.bisect_right(instructions[i])
            
            cnt += min(left, len(A)-right)
            
            A.add(instructions[i])
                
        return cnt % MOD
