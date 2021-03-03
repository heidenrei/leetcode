class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        maxi = -1
        ans = []
        for i in range(N)[::-1]:
            ans.append(maxi)
            maxi = max(maxi, arr[i])
            
        return ans[::-1]