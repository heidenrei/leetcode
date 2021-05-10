class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        # sieve
        comps = set()
        primes = set([2])
        for x in range(3, n, 2):
            if x not in comps:
                primes.add(x)
                curr = x
                while curr < n:
                    comps.add(curr)
                    curr += x
                    
        return len(primes)