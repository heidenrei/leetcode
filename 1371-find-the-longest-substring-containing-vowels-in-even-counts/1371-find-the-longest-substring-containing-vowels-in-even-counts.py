class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        N = len(s)
        best = 0
        d = defaultdict(int) # key is 5 bit bm representing cardinality of vowels
        #d[0] = -1
        bm = 0
        vowels = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
        for i, x in enumerate(s):
            if bm not in d:
                d[bm] = i
            if x in vowels:
                idx = vowels[x]
                bm ^= 1<<idx
            
            if bm in d:
                tmp = i - d[bm] + 1
                if tmp > best:
                    best = tmp
                    #print(i, s[i], d[bm])
            # else:
            #     d[bm] = i
        #print(d)
        return best