class Solution:
    def partitionString(self, s: str) -> int:
        curr = set()
        ans = 1
        for x in s:
            if x in curr:
                curr = set([x])
                ans += 1
            else:
                curr.add(x)
        return ans