class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        nums.sort(reverse=True)
        def is_good(total):
            rem = total
            for num in nums:
                if total * y >= num:
                    return True
                elif rem*x < num - (total-rem)*y:
                    return False
                else:
                    num -= (total-rem)*y
                    needed = ceil((num-rem*y)/(x-y))
                    if needed > rem:
                        return False
                    else:
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
                            
                    