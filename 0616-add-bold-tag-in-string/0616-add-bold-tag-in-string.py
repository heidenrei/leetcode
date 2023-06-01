class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        N = len(s)
        intervals = [] # [)
        words = set(words)
        for i in range(N):
            for j in range(i+1, N+1):
                if s[i:j] in words:
                    intervals.append([i, j])
        
        ints = []
        ans = ''
        intervals.sort()
        if not intervals:
            return s
        st, e = intervals[0][0], intervals[0][1]
        for x, y in intervals[1:]:
            if x <= e:
                e = max(y, e)
            else:
                ints.append([st, e])
                st, e = x, y
        ints.append([st, e])
        ints.reverse()
        for i, x in enumerate(s):
            if ints and ints[-1][0] == i:
                ans += '<b>'
            if ints and ints[-1][1] == i:
                ans += '</b>'
                ints.pop()
            ans += x

        if ints:
            ans += '</b>'
        return ans