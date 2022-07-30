class Solution:
    def findMinMoves(self,nums):
        N = len(nums)
        k = sum(nums)//N
        if sum(nums) % N:
            return -1
        to_right = 0
        ans = 0
        for x in nums:
            to_right += x - k
            ans = max(ans, abs(to_right), x - k)
            
        return ans