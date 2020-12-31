class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for dom in cpdomains:
            split_input = dom.split(' ')
            
            domains = split_input[1].split('.')[::-1]
            count = int(split_input[0])
            
            curr = ''
            
            for i in range(len(domains)):
                if i > 0:
                    curr = domains[i] + '.' + curr
                else:
                    curr = domains[i]
                    
                d[curr] += count
            
            
            ans = []
            
        for k, v in d.items():
            ans.append(' '.join([str(v), k]))
​
        return ans
​
