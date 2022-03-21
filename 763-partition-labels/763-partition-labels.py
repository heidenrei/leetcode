class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i, x in enumerate(s):
            last[x] = i
        
        start = 0
        end = 0
        ans = []
        for i, x in enumerate(s):
            end = max(end, last[x])
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
                end = i + 1
        return ans
                