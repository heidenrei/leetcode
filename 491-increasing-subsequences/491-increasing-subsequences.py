class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for x in range(3, 2**len(nums)):
            if x.bit_count() >= 2:
                A = []
                good = True
                for i in range(len(nums)):
                    if not good:
                        break
                    if x & (1<<i):
                        A.append(nums[i])
                        if len(A) >= 2 and A[-1] < A[-2]:
                            good = False
                            break
                if good:
                    ans.add(tuple(A))
                    
        return list(ans)