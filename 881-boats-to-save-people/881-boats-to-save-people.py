class Solution:
    def numRescueBoats(self, nums: List[int], k: int) -> int:
        # match heaviest with heaviest person they can go with
        nums.sort()
        nums = deque(nums)
        ans = 0
        while nums:
            left = nums.popleft()
            if nums:
                right = nums.pop()
            else:
                right = 0
            if left + right <= k:
                ans += 1
            else:
                nums.appendleft(left)
                ans += 1
                
        return ans