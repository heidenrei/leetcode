class Solution:
    def countBits(self, n: int) -> List[int]:
        return [x.bit_count() for x in range(n+1)]