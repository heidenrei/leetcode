class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)
        ans = 0
        curr = colors[0]
        starti = 0
        for i, x in enumerate(colors[1:]):
            i += 1
            if x != curr:
                if starti is not None:
                    tmp = sorted(neededTime[starti:i])
                    ans += sum(tmp[:-1])
                    #print(curr, tmp)
                    curr = x
                    starti = i
        if curr is not None:
            tmp = sorted(neededTime[starti:i+1])
            ans += sum(tmp[:-1])
            #print(curr, tmp)
        return ans
                    