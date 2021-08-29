class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        N = len(nums)
        maxi = 0
        ans = 0
        added = []
        
        for x in nums:
            while x > maxi + 1 and maxi < n:
                ans += 1
                added.append(maxi+1)
                maxi += maxi + 1
            maxi += x
            if maxi >= n:
                break
        
        while maxi < n:
            ans += 1
            added.append(maxi+1)
            maxi += maxi + 1
        #print(added)

        return ans