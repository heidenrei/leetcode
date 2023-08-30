class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums.reverse()
        prev = nums[0]
        ans = 0

        def find_d(x, prev):
            l, r = 1, x
            while l <= r:
                m = l + r >>1
                if ceil(x/m) <= prev:
                    r = m - 1
                else:
                    l = m + 1
            return floor(x/(r+1))
        
        for x in nums[1:]:
            if x > prev:
                if not x % prev:
                    ans += x//prev -1
                else:
                    d = find_d(x, prev)
                    ans += x//prev
                    prev = d
            else:
                prev = x
        return ans