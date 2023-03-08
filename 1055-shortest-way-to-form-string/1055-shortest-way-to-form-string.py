class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ans = i = j = 0
        N, M = len(source), len(target)
        ss = set([x for x in source])
        st = set([x for x in target])
        if not st.issubset(ss):
            return -1
        while j < M:
            ans += i == 0
            if source[i] == target[j]:
                i += 1
                j += 1
            else:
                i += 1
            i %= N
        return ans