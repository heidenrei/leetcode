class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        za = list(zip(plantTime, growTime))
        za.sort(key=lambda x: (x[0]-x[1], -x[1]))
        za.sort(key=lambda x: -x[1])
        ans = 0
        s = 0
        for x, y in za:
            s += x
            ans = max(ans, s+y)
        return ans
                
"""
[15,29,24,1]
[26,20,10,2]
"""