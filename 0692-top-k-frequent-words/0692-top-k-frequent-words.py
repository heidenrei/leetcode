class Solution:
    def topKFrequent(self, words: List[str], kk: int) -> List[str]:
        c = Counter(words)
        sk = sorted(c.keys())
        sc = sorted(list(set(c.values())))
        d = defaultdict(list)
        for k, v in c.items():
            d[v].append(k)
        ans = []
        while sc:
            cc = sc.pop()
            d[cc].sort()
            for x in d[cc]:
                ans.append(x)
                if len(ans) == kk:
                    return ans