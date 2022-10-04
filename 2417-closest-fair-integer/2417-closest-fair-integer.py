class Solution:
    def closestFair(self, n: int) -> int:
        if n <= 10:
            return 10
        c = Counter()
        sn = [x for x in str(n)]
        N = len(sn)
        if N & 1:
            ans = '1' + ('0'*(N//2+1)) + ('1'*(N//2))
            best = int(ans)
            return best
        for _ in range(10**5+1):
            sn = [x for x in str(n)]
            #print(sn)
            c = Counter()
            for x in sn:
                c[int(x)%2] += 1
            #print(c)
            if c[0] == c[1]:
                #print(n)
                return n
            n += 1
        sn = [x for x in str(n)]
        N = len(sn)
        if N & 1:
            ans = '1' + ('0'*(N//2+1)) + ('1'*(N//2))
        return ans
            