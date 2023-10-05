class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [k for k in c if c[k] > len(nums)/3]