class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.A = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.A.append(val)
            self.d[val] = len(self.A)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            idx = self.d[val]
            if idx == len(self.A) - 1:
                self.A.pop()
                del self.d[val]
                return True
            num = self.A.pop()
            self.A[idx] = num
            self.d[num] = idx
            del self.d[val]
            return True
        return False
            

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.A)-1)
        return self.A[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()