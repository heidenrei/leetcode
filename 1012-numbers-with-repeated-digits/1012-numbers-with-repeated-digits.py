class Solution:
    def numDupDigitsAtMostN(self, num: int) -> int:
        # num - nums without repeating digits
        snum = str(num)
        n = len(snum)
        #s = set()
        dp = defaultdict(int)
        #@cache
        def go(i, bm, smaller):
            h = (i, bm, smaller)
            if h in dp:
                return dp[h]
            #s.add((i, bm, smaller))
            if i == n:
                return 1 if bm else 0
            if bm == 2**10-1:
                dp[h] = 0
                return 0
            ans = 0
            if not bm:
                if '0' < snum[i]:
                    ans += go(i+1, bm, True)
                else:
                    ans += go(i+1, bm, smaller)
            if bm and not bm & 1:
                if '0' < snum[i]:
                    ans += go(i+1, bm | 1, True)
                else:
                    ans += go(i+1, bm | 1, smaller)

            if smaller:
                for j in range(1, 10):
                    if not bm & (1<<j):
                        ans += go(i+1, bm | (1<<j), smaller)
            else:
                for j in range(1, 10):
                    if not bm & (1<<j) and str(j) < snum[i]:
                        ans += go(i+1, bm | (1<<j), True)
                    elif (not bm & (1<<j) and str(j) == snum[i]):
                        ans += go(i+1, bm | (1<<j), smaller)
            dp[h] = ans
            return ans
        go(0, 0, False)
        #print(len(s))
        return num - go(0, 0, False)