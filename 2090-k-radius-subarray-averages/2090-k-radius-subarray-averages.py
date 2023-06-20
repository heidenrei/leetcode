class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        #print(32//7)
        if k*2+1 > N:
            return [-1]*N
        if k == 0:
            return nums
        
        ans = [-1]*k
        curr = sum(nums[:k*2])
        #print(nums[:k*2])
        for i in range(k*2, N):
            curr += nums[i]
            #print(nums[i])
            #print(curr)
            ans.append(curr//(k*2+1))
            curr -= nums[i-(k*2)]
            #print(nums[i-(k*2)])
            # if i + 1 < N:
            #     curr += nums[i+1]
            #print()
        
        ans.extend([-1]*k)
        return ans