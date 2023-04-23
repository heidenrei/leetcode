class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        N = len(nums)
        pfs = list(accumulate(nums))
        d = defaultdict(set) # sums to middle (j)
        # nest for loop for i and j, bs for k
        for i in range(1, N): #
            one = pfs[i-1]
            for j in range(i+2, N):
                two = pfs[j-1] - pfs[i]
                if one == two:
                    d[one].add(j)
        nums.reverse()
        pfs = list(accumulate(nums))
        for i in range(1, N):
            one = pfs[i-1]
            for j in range(i+2, N):
                two = pfs[j-1] - pfs[i]
                if one == two:
                    nj = N - j - 1
                    if nj in d[one]:
                        return True
        
        return False
                        
        