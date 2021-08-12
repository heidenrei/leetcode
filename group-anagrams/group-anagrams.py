class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        
        for i, s in enumerate(strs):
            c[tuple(list(sorted([x for x in s])))].append(i)
            
        ans = []
        
        for k, v in c.items():
            ans.append([strs[i] for i in v])
            
        return ans