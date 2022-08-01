class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c = Counter(s)
        s = [x for x in s]
        #print(c)
        odds = 0
        evens = 0
        for ke, v in c.items():
            if v & 1:
                odds += 1
            evens += v//2
        print(odds, evens)
        if odds > k:
            return False
        k -= odds
        if evens >= k:
            return True
        # need to split evens
        while k > evens:
            if not evens:
                return False
            k -= 2
            evens -= 1
        
        print('111', )
        if evens * 2 < k:
            return False
        return True