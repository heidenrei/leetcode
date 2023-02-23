from sortedcontainers import SortedList

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        A = list(zip(capital, profits))
        N = len(A)
        A.sort(key=lambda x: (-x[0], x[1]))
        #print(A)
        sl = SortedList()
        while A and k:
            if A and A[-1][0] <= w:
                while A and A[-1][0] <= w:
                    #print(A[-1])
                    sl.add(A[-1][1])
                    A.pop()
            if k and sl:
                k -= 1
                w += sl.pop()
            else:
                break
        
        while k and sl:
            w += sl.pop()
            k -= 1
        
        return w
            