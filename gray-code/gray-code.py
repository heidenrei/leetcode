class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for x in range(2**n):
            res.append(x^(x>>1))
            
        return res
                        
                
            
            
            
        
        
        
        