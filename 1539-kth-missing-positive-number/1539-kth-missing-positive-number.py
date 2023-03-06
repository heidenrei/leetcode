class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        for x in range(1, 2002):
            if x not in s:
                k -= 1
                if not k:
                    return x