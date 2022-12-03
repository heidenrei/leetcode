class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = [x for x in s]
        d = defaultdict(list) # key is the count, d[count][i] is a letter
        
        for k, v in c.items():
            d[v].append(k)
            
        keys = [x for x in d.keys()]
        keys.sort(reverse=True)
        ans = ''
        for k in keys:
            for ch in d[k]:
                ans += ch*k
        return ans