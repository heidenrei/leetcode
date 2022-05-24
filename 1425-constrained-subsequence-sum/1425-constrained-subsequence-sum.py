from sortedcontainers import SortedList

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        s = sum([x for x in nums if x > 0])
        if max(nums) <= 0:
            return max(nums)
        best = 0
        tmp = 0
        for key, v in groupby(nums, key=lambda x: x < 0):
            v = list(v)
            if v[0] < 0:
                #print(v)
                if len(v) >= k:
                    sl = SortedList(v[:k])
                    #print(sl)
                    for i in range(k, len(v)):
                        tv = sl[-1] + v[i]
                        sl.add(tv)
                        v[i] = tv
                        sl.remove(v[i-k])
                    tmp += sl[-1]
                    #print(sl)
                tmp = max(tmp, 0)
            else:
                tmp += sum(v)
                if tmp > best:
                    best = tmp
                    
        return best