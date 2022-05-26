class Solution:
    def hammingWeight(self, n: int) -> int:
        return int(n).bit_count()