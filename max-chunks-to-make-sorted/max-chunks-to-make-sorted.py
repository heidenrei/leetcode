class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        sorted_arr = sorted(arr)
        ans = 0
        s = set()
        for i in range(N):
            if arr[i] != sorted_arr[i]:
                if sorted_arr[i] in s:
                    s.remove(sorted_arr[i])
                if arr[i] > sorted_arr[i]:
                    s.add(arr[i])
            if not s:
                ans += 1
                
        return ans