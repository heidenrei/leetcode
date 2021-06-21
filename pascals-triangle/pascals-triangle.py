class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, len(ans[i-1])):
                tmp.append(ans[i-1][j] + ans[i-1][j-1])
            
            tmp += [1]
            ans.append(tmp)
        
        return ans