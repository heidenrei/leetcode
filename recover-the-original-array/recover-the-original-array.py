class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        # each low num has a high pair that is 2k higher than it
        cands = set()
        
        N = len(nums)
        for j in range(N-1):
            if (nums[-1] - nums[j]) % 2 == 0:
                cands.add((nums[-1] - nums[j]))
        
        if 0 in cands:
            cands.remove(0)
                
        #print(cands)
        for k in cands:
            ans = []
            tc = Counter(nums)
            good = True
            for x in nums:
                if tc[x] > 0:
                    if x + k in tc:
                        tc[x] -= 1
                        tc[x+k] -= 1
                        ans.append(x+k//2)
                    else:
                        good = False
                        break
                        
            if good:
                break
                
        return ans
            
#         for i in range(1, N-1):
#             tcands = set()
#             for j in range(i):
#                 if (nums[i] - nums[j]) % 2 == 0:
#                     tcands.add((nums[i] - nums[j]) // 2)
                    
#             cands ^= tcands
            
#         print(cands)