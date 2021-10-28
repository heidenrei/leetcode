class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        C = Counter(nums)
        nums2 = []

        if C[0] > 3:
            C[0] = 3
        
        nums2.extend([0]*C[0])
        
        for k, v in C.items():
            if k != 0:
                nums2.extend([k]*min(v, 2))
        
        nums = nums2
        
        N = len(nums)
        ans = set()
        nums.sort()
        for i in range(N):
            target = -nums[i]
            d = defaultdict(int)
            for j in range(i+1, N):
                tmp = [nums[i], nums[j], nums[d[nums[j]]]]
                if d[nums[j]]:
                    tmp.sort()
                    ans.add(tuple(tmp))
                d[target - nums[j]] = j
            
        return ans