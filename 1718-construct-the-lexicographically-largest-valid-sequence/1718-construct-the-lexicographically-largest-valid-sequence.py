class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [None for x in range(2*n-1)]
        # ans[0] =5
        # ans[5] = 5
        # ans[1] = 3
        # ans[4] = 3
        N = len(ans)
        found_ans = False
        def dfs(i):
            #print(ans)
            nonlocal ans, found_ans
            #print(ans)
            if i == N or found_ans:
                found_ans = True
                return True
            if ans[i] is None:
                used = set([x for x in ans if x is not None])
                good = sorted(list(used ^ set(range(1, n+1))), reverse=True)
                for num in good:
                    #print(num)
                    if (i + num < N and ans[i+num] is None) or num == 1:
                        ans[i] = num
                        if num != 1:
                            ans[i+num] = num
                        if dfs(i+1):
                            return True
                        else:
                            ans[i] = None
                            if num != 1:
                                ans[i+num] = None
            elif dfs(i+1):
                return True
            return False
            
                            
        dfs(0)
        return ans