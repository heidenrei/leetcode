class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(candiesCount)
        ans = [None for x in range(len(queries))]
        tq = []
        for i in range(len(queries)):
            tq.append(queries[i] + [i])
        #queries.sort(key=lambda x: x[1])
        tq.sort()
        queries = tq
        s = 0
        curr_t = 0
        for t, d, c, i in queries:
            # eat cap every day before...
            while t > curr_t:
                s += candiesCount[curr_t]
                curr_t += 1
            if s%c== 0:
                min_day = s//c
            else:
                min_day = s//c
            max_day = s + candiesCount[t] - 1
            #print(i, min_day, max_day)
            if min_day <= d <= max_day:
                ans[i] = True
            else:
                ans[i] = False
        return ans