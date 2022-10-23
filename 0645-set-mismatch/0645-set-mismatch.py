class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        zero = set(nums) ^ set(range(1, len(nums)+1))
        c = Counter(nums)
        two = set([x for x in nums if c[x] == 2])
        return list(two) + list(zero)