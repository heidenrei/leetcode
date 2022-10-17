class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # need pfs == sfs
        N = len(nums)
        i = 0
        j = N-1
        pfs = 0
        sfs = 0
        ans = 0
        while i <= j:
            #print(pfs, sfs)
            if pfs < sfs:
                pfs += nums[i]
                i += 1
                ans += 1
            elif sfs < pfs:
                sfs += nums[j]
                j -= 1
                ans += 1
            else:

                pfs += nums[i]
                sfs += nums[j]
                i += 1
                j -= 1
        
        if pfs != sfs:
            ans += 1
        return ans