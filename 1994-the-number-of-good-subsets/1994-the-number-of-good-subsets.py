class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = 10**9+7
        N = len(nums)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        d = defaultdict(int)
        for i in range(10):
            d[primes[i]] = i
        
        def pc(x):
            ans = []
            for p in primes:
                while x % p == 0:
                    x //= p
                    ans.append(p)
            return ans
        
        cnum = Counter(nums)
        nums = sorted(list(set(nums)))
        N = len(nums)
        
        @cache
        def go(i, bm, num_bm):
            if i == N:
                if bm == 0:
                    return 0
                else:
                    #print(bin(num_bm))
                    ans = 1
                    for j in range(N):
                        #print(j)
                        if num_bm & (1<<j):
                            #print(nums[j])
                            if nums[j] != 1:
                                ans *= cnum[nums[j]]
                                ans %= MOD
                            else:
                                ans *= (1<<cnum[nums[j]])-1
                                ans %= MOD
                    return ans
            
            ans = go(i+1, bm, num_bm)
            
            prime_d = pc(nums[i])
            good = True

            if len(set(prime_d)) != len(prime_d):
                good = False
            for x in prime_d:
                if bm & (1<<d[x]):
                    good = False
                    break
                else:
                    bm |= (1<<d[x])
            if good:
                ans += go(i+1, bm, num_bm | (1<<i))
                ans %= MOD
                    
            return ans % MOD
        
        return go(0, 0, 0)
        
                