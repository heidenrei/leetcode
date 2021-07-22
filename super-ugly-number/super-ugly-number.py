from sortedcontainers import SortedList

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        cnt = 1
        curr = 1
        nums = SortedList(primes)
        seen = set()
        while cnt < n:
            curr = nums.pop(0)
            cnt += 1
            for p in primes:
                if p*curr not in seen:
                    seen.add(p*curr)
                    nums.add(p*curr)
        return curr