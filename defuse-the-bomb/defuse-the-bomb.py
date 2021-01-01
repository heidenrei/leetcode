class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        ans = [0]*N
​
        if k == 0:
            return ans
        
        if k < 0:
            code.reverse()
            
        code = deque(code)
        
        for i in range(N):
            tmp = code
            sumi = 0
            for j in range(abs(k)):
                sumi += code[(i+j+1) % N]
            
            ans[i] = sumi
        
        return ans if k > 0 else ans[::-1]
