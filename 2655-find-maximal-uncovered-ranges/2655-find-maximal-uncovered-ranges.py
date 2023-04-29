class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        events = [[n, 0]]
        for x, y in ranges:
            events.append([x, 0])
            events.append([y, 1])
        events.sort()
        opn = 0
        opn_idx = -1
        added = set()
        ans = []
        for x, t in events:
            if t == 0 and not opn and x-1 not in added:
                added.add(x-1)
                ans.append([opn_idx+1, x-1])
            if t == 1 and opn == 1:
                opn_idx = x
            if t == 0:
                opn += 1
            else:
                opn -= 1
        
        ret = []
        for x in ans:
            if not x[0] > x[1]:
                ret.append(x)
        return sorted(ret)#, key=lambda x: -(x[1] - x[0]))