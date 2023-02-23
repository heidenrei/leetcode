class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9+7
        # pf cant have any even exponents
        primes = [2,3,5,7,11,13,17,19,23,29]
        c = Counter(nums)
        nums = list(set(nums))
        d = defaultdict(int)
        is_square = set()
        @cache
        def pf(x):
            ogx = x
            ans = 0
            ind = defaultdict(int)
            for i, p in enumerate(primes):
                while x % p == 0:
                    ans ^= 1<<i
                    ind[p] += 1
                    if ind[p] > 1:
                        is_square.add(ogx)
                        return
                    x //= p
                    if x == 1:
                        break
            return ans
        for x in nums:
            pf(x)
            
        nums = [x for x in nums if x not in is_square]
        if 1 in nums:
            nums.remove(1)
        
        N = len(nums)
        @cache
        def go(i, bm):
            if i == N:
                return 1
            ans = go(i+1, bm) % MOD
            tmp = pf(nums[i])
            
            if not tmp & bm:
                ans += go(i+1, tmp | bm) * c[nums[i]]
                ans %= MOD
                
            return ans 
        return ((pow(2, c[1], MOD) * go(0, 0)) - 1 ) % MOD
            