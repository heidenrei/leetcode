class Solution:
    def countPairs(self, nums: List[int]) -> int:
        MOD = 10**9+7
        
        cnt = 0
        
        powers = []
        seen = set()
        c = Counter(nums)
        
        nums = list(set(nums))
        N = len(nums)
        
        for x in range(1, 41):
            powers.append(2**x)
            
        for i in range(N):
            for p in powers:
                if nums[i] < p:
                    if p - nums[i] in seen:
                        print(nums[i], p - nums[i])
                        cnt += c[p - nums[i]] * c[nums[i]]
                    seen.add(nums[i])
                
        for k, v in c.items():
            if k != 0 and math.log2(k*2) % 1 == 0 and v >= 2:
                cnt += math.floor(math.factorial(c[k])/(math.factorial(2) * math.factorial(c[k]-2)))
                
        if 0 in nums:
            for num in nums:
                if num != 0 and math.log2(num) % 1 == 0:
                    cnt += c[0] * c[num]
        
        return cnt % MOD
