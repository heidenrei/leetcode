class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        target = N / 4
        c = Counter(arr)
        for k, v in c.items():
            if v > target:
                return k
            
        return -1