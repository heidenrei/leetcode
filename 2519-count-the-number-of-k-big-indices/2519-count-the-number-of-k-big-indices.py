class BIT:
    def __init__(self, list):
        """"Initialize BIT with list in O(n)"""
        self.array = [0] + list
        for idx in range(1, len(self.array)):
            idx2 = idx + (idx & -idx)
            if idx2 < len(self.array):
                self.array[idx2] += self.array[idx]

    def prefix_query(self, idx):
        """Computes prefix sum of up to including the idx-th element"""
        idx += 1
        result = 0
        while idx:
            result += self.array[idx]
            idx -= idx & -idx
        return result

    def range_query(self, from_idx, to_idx):
        """Computes the range sum between two indices (both inclusive)"""
        return self.prefix_query(to_idx) - self.prefix_query(from_idx - 1)

    def update(self, idx, add):
        """Add a value to the idx-th element"""
        idx += 1
        while idx < len(self.array):
            self.array[idx] += add
            idx += idx & -idx

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        N = len(nums)
        for i, x in enumerate(nums):
            d[x].append(i)
        
        b = BIT([0]*(N+1))
        ans = 0
        for key in sorted(list(d.keys())):
            for i in d[key]:
                if b.range_query(0, i) >= k and b.range_query(i, N) >= k:
                    ans += 1
            for i in d[key]:
                b.update(i, 1)
                
        return ans