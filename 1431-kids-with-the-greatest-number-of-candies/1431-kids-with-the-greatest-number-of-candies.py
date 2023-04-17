class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        ans = []
        for x in candies:
            if x + extraCandies >= maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans