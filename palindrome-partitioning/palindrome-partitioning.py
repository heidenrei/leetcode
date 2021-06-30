class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []
        def is_pal(x):
            return x == x[::-1]
        
        def go(i, curr):
            if i == N:
                ans.append(curr)
            
            curr = list(curr)
            
            for length in range(1, N-i+1):
                if is_pal(s[i:i+length]):
                    curr.append(s[i:i+length])
                    go(i+length, tuple(curr))
                    curr.pop()
                        
        go(0, [])
        
        return ans