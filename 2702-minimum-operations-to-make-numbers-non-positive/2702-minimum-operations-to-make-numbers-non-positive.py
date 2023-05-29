class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        nums.sort(reverse=True)
        d = x - y
        def is_good(total):
            rem = total
            for num in nums:
                num -= (total-rem)*y + rem*y
                needed = ceil(num/d)
                if needed > rem:
                    return False
                rem -= needed
            return True

        l, r = 0, 10**9
        while l <= r:
            m = l + r >> 1
            if is_good(m):
                r = m - 1
            else:
                l = m + 1
        return r + 1
                            
                    