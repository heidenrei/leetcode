class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = Counter([x for x in s])
        ans = 0
        threes = 0
        twos = 0
        freqs = []
        for k, v in c.items():
            freqs.append([k,v])
        freqs.sort(key=lambda x: -x[1])
        cost = defaultdict(int)
        for k, v in freqs:
            if threes < 9:
                ans += v
                threes += 1
            elif twos < 9:
                ans += v*2
                twos += 1
            else:
                ans += v*3
                
        return ans
                