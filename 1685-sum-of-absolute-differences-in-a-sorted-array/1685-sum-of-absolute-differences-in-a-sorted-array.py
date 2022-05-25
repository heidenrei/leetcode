class BIT:
    """Implementation of a Binary Indexed Tree (Fennwick Tree)"""
    
    #def __init__(self, list):
    #    """Initialize BIT with list in O(n*log(n))"""
    #    self.array = [0] * (len(list) + 1)
    #    for idx, val in enumerate(list):
    #        self.update(idx, val)

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
    def getSumAbsoluteDifferences(self, nums):
        N = len(nums)
        b = BIT(nums)
        ans = []
        for i, x in enumerate(nums):
            left_rs = b.range_query(0, i-1)
            right_rs = b.range_query(i+1, N-1)
            left_cnt = i
            right_cnt = N - i - 1
            ans.append(nums[i]*left_cnt - left_rs)
            ans[-1] += right_rs - nums[i]*right_cnt
            
        return ans