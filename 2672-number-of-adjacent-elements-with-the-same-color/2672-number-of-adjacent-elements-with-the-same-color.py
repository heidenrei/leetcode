from sortedcontainers import SortedList

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        sl = SortedList()
        cnt = 0
        ans = []
        a = [0]*n
        
        for i, c in queries:
            if a[i] == c:
                ans.append(cnt)
                continue
            a[i] = c
            
            idx = sl.bisect([i, inf, i])
            
            if idx > 0 and sl[idx-1][0] <= i <= sl[idx-1][2] and sl[idx-1][1] != c:
                tmpl = [sl[idx-1][0], sl[idx-1][1], i-1]
                tmpr = [i+1, sl[idx-1][1], sl[idx-1][2]]
                cnt -= sl[idx-1][2] - sl[idx-1][0]
                sl.pop(idx-1)
                if tmpl[2] >= tmpl[0]:
                    sl.add(tmpl)
                    cnt += tmpl[2] - tmpl[0]
                if tmpr[2] >= tmpr[0]:
                    sl.add(tmpr)
                    cnt += tmpr[2] - tmpr[0]

            # check if it merges to the right
            #idx = sl.bisect([i, -inf, i])
            l, r = i, i
#             if idx < len(sl) and sl[idx][0] <= i+1 and sl[idx][1] == c:
#                 r = sl[idx][2]
#                 cnt -= sl[idx][2] - sl[idx][0]

#                 sl.pop(idx)
            idx = sl.bisect([i, inf, i])
            if idx > 0 and sl[idx-1][2] >= i-1 and sl[idx-1][1] == c:
                l = sl[idx-1][0]
                cnt -= sl[idx-1][2] - sl[idx-1][0]
                sl.pop(idx-1)
            idx = sl.bisect([i, inf, i])
            if idx < len(sl) and sl[idx][0] <= i+1 and sl[idx][1] == c:
                r = sl[idx][2]
                cnt -= sl[idx][2] - sl[idx][0]
                sl.pop(idx)

            cnt += r - l
            sl.add([l,c,r])
            #print(sl)
            #print(a)
            #print(i, c)
            #print()
            ans.append(cnt)

        return ans