class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones];heapify(h)
        N = len(stones)
        while N > 1:
            x = -heappop(h)
            y = -heappop(h)
            N -= 2
            if x < y:
                heappush(h, -(y - x))
                N += 1
            elif x > y:
                heappush(h, -(x - y))
                N += 1
        
        if not N:
            return 0
        else:
            return -heappop(h)
        