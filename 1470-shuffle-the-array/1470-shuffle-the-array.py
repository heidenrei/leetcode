class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        N = len(nums)//2
        l = nums[:N]
        r = nums[N:]
        ans = []
        for i in range(N):
            ans.append(l[i])
            ans.append(r[i])
        return ans