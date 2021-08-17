from sortedcontainers import SortedList

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        sl = SortedList()
        ans = 0
        c = Counter(ages)
                
        for x in ages:
            ans += sl.bisect_right(x) - sl.bisect_right(0.5 * x + 7)
            sl.add(x)
            
        return ans + sum([(x*(x-1))//2 for k, x in c.items() if not k <= 0.5 * k + 7])
            