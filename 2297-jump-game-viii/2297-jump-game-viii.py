class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        # each index has max 2 edges (next bigger or equal, next smaller)
        N = len(nums)
        mq1 = []
        mq2 = []
        dp = [inf]*N
        dp[0] = 0
        ng = defaultdict(list)
        ns = defaultdict(list)
        for i, x in enumerate(nums):
            while mq1 and mq1[-1][0] <= x:
                #ng[mq1[-1][1]] = i
                ng[i].append(mq1[-1][1])

                mq1.pop()
            # if mq1:
            #     ng[mq1[-1][1]] = i
            
            while mq2 and mq2[-1][0] > x:
                #ns[mq2[-1][1]] = i
                ns[i].append(mq2[-1][1])
                mq2.pop()
            # if mq2:
            #     ns[mq2[-1][1]] = i
            mq1.append([x, i])
            mq2.append([x, i])
            
        for i in range(N):
            for x in ng[i]:
                dp[i] = min(dp[i], dp[x] + costs[i])
            for x in ns[i]:
                dp[i] = min(dp[i], dp[x] + costs[i])
        
        #print(ns)
        #print(ng)
       # 
       # print(dp)
        
        return dp[-1]