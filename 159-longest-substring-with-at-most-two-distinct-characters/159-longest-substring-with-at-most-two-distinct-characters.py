class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        N = len(s)
        i, j = 0, 1
        best = 1
        c = Counter(s[0])
        while j < N:
            #print('000', i, j)
            while j < N and len(c.keys()) <= 2:
                #print('111')
                c[s[j]] += 1
                j += 1
                if len(c.keys()) <= 2:
                    best = max(best, j - i)
            while len(c.keys()) > 2:
                #print('222')
                c[s[i]] -= 1
                if c[s[i]] == 0:
                    del c[s[i]]
                i += 1
                if len(c.keys()) == 2:
                    #print(c)
                    #@if j - i > best:
                        #print('44444', s[i:j])
                    best = max(best, j - i)
            # if len(c.keys()) <= 2:
            #     print(s[i:j])
            #     best = max(best, j - i)
        return best