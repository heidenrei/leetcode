class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        
        def go(n):
            if n == 1:
                return
            
            nonlocal cnt
​
            cnt += n//2
            if n & 1:
                go(n//2+1)
            else:
                go(n//2)
                    
        go(n)
        
        return cnt
            
