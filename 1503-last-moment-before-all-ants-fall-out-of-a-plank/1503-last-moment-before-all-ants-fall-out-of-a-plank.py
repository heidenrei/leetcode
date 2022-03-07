class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort(reverse=True)
        right.sort()
        if not left and not right:
            return 0
        if not left:
            return n - right[0]
        if not right:
            return left[0]
        return max(n - right[0], left[0])
        