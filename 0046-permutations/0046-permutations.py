class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list([list(x) for x in permutations(nums)])