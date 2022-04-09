from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        
        for n in nums:
            c[n] += 1
        
        out = []
        
        for ki, v in c.items():
            out.append([ki, v])
            
        out = sorted(out, key=lambda x: x[1], reverse=True)
        
        print(out)
        
        return [x[0] for x in out[:k]]