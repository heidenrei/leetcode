class Solution:
    def confusingNumberII(self, n: int) -> int:
        # 609 -> not confusing
        # 808 -> not confusing
        
        # number of numbers that:
        # dont have 2,3,4,5,7
        # 0,1,8 must be in palindrome positions/mirrored
        # 6,9 must be in palindrome positions/mirrored with the opposite.. cant be in the middle position
        norms = [0,1,8]
        sn = [6,9]
        nums = [0,1,8,6,9]
        nums = [str(x) for x in nums]
        mirror = {'6':'9','9':'6','0':'0','8':'8','1':'1'}
        
        def is_confusing(s):
            #print(s)
            N = len(s)
            if N&1 and s[N//2] in ['6','9']:
                return True
            #has_num = not all([x == '0' for x in s])
            for i in range(len(s)//2):
                bi = N-i-1
                if mirror[s[bi]] != s[i]:
                    return True
            return False
        
#         for x in range(1, n+1):
#             if is_confusing()
        
        ans = 0
        max_n = len(str(n))
        #@cache
        def dfs(x):
            if int(x) > n or len(x) > max_n:
                return
            if is_confusing(x):
                #print(x)
                nonlocal ans
                ans += 1
            for y in nums:
                dfs(x+y)
                
        for y in nums[1:]:
            dfs(str(y))
            
        return ans
            