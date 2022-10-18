class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        nums = []
        N = len(nums1)
        for i in range(N):
            nums.append(abs(nums1[i] - nums2[i]))
        k = k1 + k2
        nums.sort()
        if k >= sum(nums):
            return 0
        # monotonically increasing
        # want max as low as possible
        def is_good(maxi):
            rem = k
            for x in nums:
                if x > maxi:
                    rem -= x - maxi
                    if rem < 0:
                        return False
            return True
        
        l, r = 0, max(nums)
        while l <= r:
            m = l + r >> 1
            if is_good(m):
                r = m - 1
            else:
                l = m + 1
        maxi = r + 1
        ans = 0
        cnt = 0
        for x in nums:
            if x < maxi:
                ans += x**2
            else:
                k -= x - maxi
                cnt += 1
        for _ in range(cnt):
            if k:
                k -= 1
                ans += (maxi-1)**2
            else:
                ans += maxi**2
        return ans