from sortedcontainers import SortedList

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        used = set()
        N = len(strs)
        left = ''
        right = []
        for x in strs:
            if x[::-1] > x:
                right.append(x[::-1])
            else:
                right.append(x)
        #print(right)
        ans = ''.join(right)
        for i in range(N):
            for j in range(len(strs[i])):
                for s in [strs[i][::-1], strs[i]]:
                    #print(s[j:] + ''.join(right[i+1:]) + left + s[:j])
                    #print('111', ''.join(right[i+1:]))
                    ans = max(ans, s[j:] + ''.join(right[i+1:]) + left + s[:j])
            x = strs[i]
            if x[::-1] > x:
                left += x[::-1]
            else:
                left += x

        return ans