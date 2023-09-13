from sortedcontainers import SortedList

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        
        sl = SortedList()
        
        ans = [None for x in range(N)]
        
        for i, x in enumerate(ratings):
            sl.add([x, i])
            
        while sl:
            currx, curridx = sl.pop(0)
            val = 1
            if curridx - 1 >= 0 and ans[curridx - 1] != None:
                if ratings[curridx] > ratings[curridx-1]:
                    val = max(val, ans[curridx - 1]+1)
                # elif ratings[curridx] == ratings[curridx-1]:
                #     val = max(val, ans[curridx - 1])
            if curridx + 1 < N and ans[curridx + 1] != None:
                if ratings[curridx] > ratings[curridx+1]:
                    val = max(val, ans[curridx +1]+1)
                # elif ratings[curridx] == ratings[curridx+1]:
                #     val = max(val, ans[curridx + 1])
                
            ans[curridx] = val
        return sum(ans)