class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        in_bloom = 0
        events = []
        for x, y in flowers:
            events.append([x, 0, 10])
            events.append([y, 2, 10])
        for i, p in enumerate(persons):
            events.append([p, 1, i])
            
        events.sort()
        ans = [0]*len(persons)
        for x, t, i in events:
            if t == 0:
                in_bloom += 1
            elif t == 2:
                in_bloom -= 1
            else:
                ans[i] = in_bloom
                
        return ans