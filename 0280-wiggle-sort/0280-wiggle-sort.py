class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        N = len(nums)
        N2 = N//2
        if N & 1:
            N2 += 1
        left = nums[:N2][::-1]
        right = nums[N2:][::-1]
        ans = []
        for i in range(N):
            if i & 1:
                ans.append(right.pop())
            else:
                ans.append(left.pop())
        for i in range(N):
            nums[i] = ans[i]
        
        