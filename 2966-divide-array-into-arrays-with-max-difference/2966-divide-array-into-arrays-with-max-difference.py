
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        c = Counter(nums)
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            ans.append(nums[i:i+3])
            if ans[-1][2] - ans[-1][0] > k:
                return []
        return ans