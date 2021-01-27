class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        N = len(s)
        st = 0
        e = 0
        
        curr = s[0]
        cnt = 1
        
        ans = []
        
        for i in range(1, N):
            if s[i] == curr:
                cnt += 1
                e += 1
            else:
                if cnt >= 3:
                    ans.append([st, e])
                curr = s[i]
                cnt = 1
                st = i
                e = i
        
        if cnt >= 3:
            ans.append([st, e])
        
        return ans
