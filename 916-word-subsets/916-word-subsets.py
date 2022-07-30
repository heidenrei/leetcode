class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        b_intersection = Counter()
        for word in B:
            f = Counter(word)
            
            for c in f.keys():
                b_intersection[c] = max(b_intersection[c], f[c])
                
        for word in A:
            f = Counter(word)
            
            if (f & b_intersection) == b_intersection:
                ans.append(word)
                
                    
        return ans