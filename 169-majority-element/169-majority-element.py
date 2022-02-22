class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        cnt = 0
        for k, v in Counter(nums).items():
            if v > cnt:
                ans = k
                cnt = v
        return ans