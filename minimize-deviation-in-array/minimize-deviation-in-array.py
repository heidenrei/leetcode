class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        INF = float('inf')
        
        smallest = INF
        
        for x in nums:
            if x % 2 == 0:
                heapq.heappush(heap, -x)
                smallest = min(smallest, x)
            else:
                heapq.heappush(heap, -(x*2))
                smallest = min(smallest, x*2)
                
        best = INF
        
        while len(heap) > 0:
            largest = -heap[0]
            
            heapq.heappop(heap)
            best = min(best, largest - smallest)
            
            if largest % 2 == 1:
                break
            else:
                heapq.heappush(heap, -(largest//2))
                smallest = min(smallest, largest//2)

                
        return best