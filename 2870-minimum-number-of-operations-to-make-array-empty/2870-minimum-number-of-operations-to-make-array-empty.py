class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for v in Counter(nums).values():
            if v == 1:
                return -1
            while v > 2:
                ans += 1
                v -= 3
            if v:
                ans += 1
                
        return ans