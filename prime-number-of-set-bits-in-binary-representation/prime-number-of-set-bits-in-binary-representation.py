class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        ans = 0
        for num in range(L, R+1):
            if sum([int(x) for x in bin(num)[2:]]) in primes:
                ans += 1
        
        return ans