class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if not s:
            return -1
        
        d = collections.defaultdict(int)
        N = len(s)
        best = 0
        
        for i in range(N):
            print(s[i], d)
            if not d[s[i]]:
                d[s[i]] = i+1
            else:
                print('here')
                best = max(best, i+1-d[s[i]])
                # d[s[i]] = i+1
                
        return best - 1 