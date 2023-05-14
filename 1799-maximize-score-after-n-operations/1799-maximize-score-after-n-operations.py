class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)
        
        def get_score(i, x, y):
            #print(i, x, y)
            return i * math.gcd(x, y)
        
        seen = set()
        
        @lru_cache(None)
        def go(bm):
            rem = Counter(bin(bm)[2:].zfill(N))['0']
            if rem <= 1:
                return 0
            i = (N - rem) // 2 + 1
            
            
            rem_nums = []
            #print(bin(bm)[2:].zfill(N))
            for idx in range(N):
                if bin(bm)[2:].zfill(N)[idx] == '0':
                    rem_nums.append(N - 1 - idx)

            maxi = 0
                        
            for idx in range(len(rem_nums)):
                for jdx in range(idx):
                    tmp = go(bm | (1 << rem_nums[idx]) | (1 << rem_nums[jdx])) + get_score(i, nums[rem_nums[idx]], nums[rem_nums[jdx]])
                    if tmp > maxi:
                        maxi = tmp
                        
            return maxi
        
        return go(0)