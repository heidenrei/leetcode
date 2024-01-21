def cp(n):
    n = str(n)
    candidates = []
    length = len(n)
    mid = (length + 1) // 2
    good = 1
    for i in range(mid):
        if n[i] != n[length-i-1]:
            good = 0
    if good:
        return n
    
    if length == 1:
        return str(int(n) - 1)
    candidates.append(10 ** length + 1)
    candidates.append(10 ** (length - 1) - 1)
    prefix = int(n[:mid])

    temp = [prefix, prefix + 1, prefix - 1]
    for i in temp:
        res = str(i)
        if length & 1:
            res = res[:-1]
        peep = str(i) + res[::-1]
        candidates.append(int(peep))
    minDiff = float('inf')
    result = tip = int(n)
    for i in range(5):
        if candidates[i] != tip and minDiff > abs(candidates[i] - tip):
            result = candidates[i]
            minDiff = abs(candidates[i] - tip)
        elif abs(candidates[i] - tip) == minDiff:
            result = min(result, candidates[i])
    return str(result)

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        N = len(nums)
        ans = inf
        def go(m):
            m = cp(m)
            m = int(m)
            return sum([abs(m - x) for x in nums])
        for di in range(-5, 6):
            i = N//2+di
            if 0 <= i < N:
                tmp = go(nums[i])
                if tmp < ans:
                    ans = tmp
                tmp = go(nums[i]+1)
                if tmp < ans:
                    ans = tmp
            if 0 <= i < i+1 < N:
                tmp = go((nums[i] + nums[i+1])//2)
                if tmp < ans:
                    ans = tmp
                tmp = go((nums[i] + nums[i+1])//2+1)
                if tmp < ans:
                    ans = tmp
        return ans