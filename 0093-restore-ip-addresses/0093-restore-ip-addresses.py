class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        ips = []
        for c in combinations(range(1, N), 3):
            ip = ''
            for i in range(N):
                if i in c:
                    ip += '.'
                ip += s[i]
            ips.append(ip)
                
        ans = []
        for ip in ips:
            blocks = ip.split('.')
            good = True
            for b in blocks:
                if len(str(int(b))) < len(b) or int(b) > 255:
                    good = False
                    
            if good:
                ans.append(ip)
        return ans