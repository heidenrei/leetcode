class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        s = sorted(c.values())
        ans = len(c.keys())
        for v in s:
            if v <= k:
                ans -= 1
                k -= v
        return ans