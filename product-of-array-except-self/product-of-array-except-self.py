class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        curr = 1
        l = [1]
        r = [1]
        for num in nums:
            curr *= num
            l.append(curr)
        
        curr = 1
        
        for num in nums[::-1]:
            curr *= num
            r.append(curr)
            
        r = r[::-1]
        
        ans = []
        
        for i in range(N):
            ans.append(l[i] * r[i+1])
            
        return ans