class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        N = len(nums)
        for x in nums:
            if x & 1:
                odds.append(x)
            else:
                evens.append(x)
                
        ans = []
        
        for i in range(N):
            if i & 1:
                ans.append(odds.pop())
            else:
                ans.append(evens.pop())
                
        return ans