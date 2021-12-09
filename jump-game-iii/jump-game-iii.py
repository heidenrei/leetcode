class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        goal = len(arr) - 1
        
        dp = [0 for x in arr]
        possible = False
        
        def go(idx):
            nonlocal possible
            # print(idx)
            # print(dp)
            if arr[idx] == 0:
                possible = True
                return
            
            back = idx - arr[idx]
            forward = idx + arr[idx]
            
            if back >= 0 and dp[back] == 0:
                dp[back] = 1
                go(back)
                
            if forward <= goal and dp[forward] == 0:
                dp[forward] = 1
                go(forward)
                
        go(start)
        
        return possible