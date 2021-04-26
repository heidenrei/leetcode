class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        arr.sort()
        ans = -1
        for i in range(len(arr)):
            if arr[i] == c[arr[i]]:
                ans = arr[i]
        return ans