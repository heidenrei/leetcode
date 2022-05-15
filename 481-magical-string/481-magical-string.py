class Solution:
    def magicalString(self, n: int) -> int:
        ans = '12211'
        ans = [1,2,2]
        i = 2
        while len(ans) < n:
            if ans[i] == 1:
                if ans[-1] == 1:
                    ans.append(2)
                else:
                    ans.append(1)
            else:
                if ans[-1] == 2:
                    ans.append(1)
                    ans.append(1)
                else:
                    ans.append(2)
                    ans.append(2)
            i += 1
        #print(ans)
        return ans[:n].count(1)