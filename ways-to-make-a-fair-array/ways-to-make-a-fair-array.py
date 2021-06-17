class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        N = len(nums)
        
        even_pfs = [0]
        odd_pfs = [0]
        
        for i in range(N):
            if i & 1:
                odd_pfs.append(nums[i] + odd_pfs[-1])
                even_pfs.append(even_pfs[-1])
            else:
                even_pfs.append(nums[i] + even_pfs[-1])
                odd_pfs.append(odd_pfs[-1])
        
        cnt = 0
        
        for i in range(1, N+1):
            even = even_pfs[i-1] + odd_pfs[-1] - odd_pfs[i]
            odd = odd_pfs[i-1] + even_pfs[-1] - even_pfs[i]
            cnt += even == odd
                
        return cnt
            