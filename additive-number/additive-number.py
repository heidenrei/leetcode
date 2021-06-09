class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        found_ans = False
        
        def go(prev1, prev2, idx):
            curr = num[idx]
            while int(curr) < prev1 + prev2:
                idx += 1
                if idx < N:
                    curr += num[idx]
                else:
                    return
            idx += 1
            
            if (curr[0] != '0' or len(curr) == 1) and int(curr) == prev1 + prev2:
                if idx == N:
                    nonlocal found_ans
                    found_ans = True
                if idx < N:
                    go(prev2, int(curr), idx)
                
        for i in range(1, N):
            for j in range(1, i):
                if (num[:j][0] != '0' or len(num[:j]) == 1) and (num[j:i][0] != '0' or len(num[j:i]) == 1):
                    go(int(num[:j]), int(num[j:i]), i)
                
        return found_ans