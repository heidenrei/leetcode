class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        ans = []
        heap = []
        last = -1
        for i in range(N-k+1):
            heapq.heappush(heap, (nums[i], i))
        i = N - k + 1
        
        for _ in range(k):
            while heap[0][1] <= last:
                heapq.heappop(heap)
                
            x, lastidx = heap[0]
            last = lastidx
            ans.append(x)
            
            if i < N:
                heapq.heappush(heap, (nums[i], i))
                i += 1
                
        return ans
