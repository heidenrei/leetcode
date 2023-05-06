from sortedcontainers import SortedList

class Solution:
    def numSubseq(self, nums: List[int], k):
        N = len(nums)
        nums.sort()
        MOD = 10**9+7
        sl = SortedList()
        ans = 0
        for x in nums:
            sl.add(x)
            lidx = sl.bisect_right(k-x)
            if not lidx:
                break
            if lidx == len(sl):
                ans += pow(2, len(sl)-1, MOD)
                continue
            #print(sl)
            #print(x)
            #print(lidx)
            tmp = pow(2, lidx, MOD)-1
            #print(tmp)
            if len(sl)-lidx-1 > 0:
                
                tmp *= pow(2, len(sl)-lidx-1, MOD)
            #print(tmp)
            ans += tmp
            ans %= MOD
        return ans