class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            out = ''
            idx = e.index('@')
            for i in range(idx):
                if e[i] == '+':
                    break
                if e[i] != '.':
                    out += e[i]
                    
            s.add(out + e[idx:])
            
        return len(s)