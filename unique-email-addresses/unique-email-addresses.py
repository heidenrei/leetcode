class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        N = len(emails)
        ans = 0
        uniques = set()
        
        for i in range(N):
            local, domain = emails[i].split('@')
            
            local = [x for x in local]
            idx = 0
            tmp = ''
            while idx < len(local):
                if local[idx] == '+':
                    break
                elif local[idx] == '.':
                    pass
                else:
                    tmp += local[idx]
                idx += 1
                    
            local = ''.join(tmp)
            if tuple([local, domain]) not in uniques:
                ans += 1
                uniques.add(tuple([local, domain]))
        return ans