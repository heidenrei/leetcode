class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        if n == k:
            return 0
        @cache
        def go(i, prev, prev_cnt, rem):
            if i == n:
                if prev_cnt == 1:
                    return 1
                else:
                    return len(str(prev_cnt)) + 1
            if s[i] == prev:
                pick = go(i+1, prev, prev_cnt+1, rem)
            else:
                if prev_cnt == 1:
                    cost = 1
                else:
                    cost = len(str(prev_cnt)) + 1
                pick = go(i+1, s[i], 1, rem) + cost
            if not rem:
                pss = inf
            else:
                pss = go(i+1, prev, prev_cnt, rem-1)
            return min(pss, pick)
        
        skip = inf
        for i in range(k):
            tmp = go(i+2, s[i+1], 1, k-i-1)
            if tmp < skip:
                skip = tmp
        return min(skip, go(1, s[0], 1, k))