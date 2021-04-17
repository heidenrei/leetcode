class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        seqs = []
        uniques = set(s)
        
        for c in uniques:
            seqs.append(c*k)
            
        
        while 1:
            tmp = s
            
            for seq in seqs:
                if seq in s:
                    s = s.replace(seq, '')
            
            if s == tmp:
                return s