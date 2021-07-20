from random import shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.og = nums[::]
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        #self.nums = self.og.copy()
        return self.og

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle(self.nums)
        return self.nums