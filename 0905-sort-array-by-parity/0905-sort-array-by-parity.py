class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odds, evens = [], []
        for x in nums:
            if x & 1:
                odds.append(x)
            else:
                evens.append(x)
        return evens + odds
