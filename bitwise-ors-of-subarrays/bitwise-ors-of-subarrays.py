class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        vals = set()
        
        for x in arr:
            vals = {x | y for y in vals} | {x}
            ans |= vals
        
        return len(ans)
        
        
        