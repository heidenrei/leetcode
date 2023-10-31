class Solution:

    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        p = 0
        for x in pref:
            ans.append(x^p)
            p ^= ans[-1]
        
        return ans