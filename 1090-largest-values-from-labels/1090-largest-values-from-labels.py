class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        nums = []
        N = len(values)
        for i in range(N):
            nums.append([values[i], labels[i]])
            
        ans = 0
        c = Counter()
        nums.sort(reverse=True)
        for i in range(N):
            if c[nums[i][1]] < useLimit:
                ans += nums[i][0]
                c[nums[i][1]] += 1
                numWanted -= 1
                if numWanted == 0:
                    break
                
        return ans