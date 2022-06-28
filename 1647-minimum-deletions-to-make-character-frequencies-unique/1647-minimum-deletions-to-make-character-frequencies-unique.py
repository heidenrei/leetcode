class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        cnts = []
        ans = 0
        for k, v in c.items():
            cnts.append(v)
            
        # cnts.sort(reverse=True)
        seen = set()
        for x in cnts:
            while x in seen and x > 0:
                ans += 1
                x -= 1
            seen.add(x)
        return ans