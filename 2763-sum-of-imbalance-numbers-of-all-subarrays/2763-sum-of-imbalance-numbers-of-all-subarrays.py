class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        for i in range(N):
            maxi = mini = nums[i]
            s = set([nums[i]])
            cnt = 0
            for j in range(i+1, N):
                if nums[j] in s:
                    ans += cnt
                    continue
                if nums[j] - 1 not in s and mini < nums[j] - 1:
                    cnt += 1
                if nums[j] + 1 not in s and maxi > nums[j] + 1:
                    cnt += 1
                if mini < nums[j] < maxi and maxi - mini > 1:
                    cnt -= 1
                s.add(nums[j])
                mini = min(nums[j], mini)
                maxi = max(nums[j], maxi)
                ans += cnt
        return ans
                
            
                