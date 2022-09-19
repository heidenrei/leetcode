class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        d = defaultdict(list)
        
        for p in paths:
            path = p.split(' ')
            for i in range(1, len(path)):
                idx = 0
                brack_open = False
                content = ''
                while idx < len(path[i]):
                    if path[i][idx] == ')':
                        brack_open = False
                    if brack_open:
                        content += path[i][idx]
                    if path[i][idx] == '(':
                        brack_open = True
                    idx += 1
                    
                d[content].append(path[0] + '/' + path[i].split('(')[0])
                
        for k, v in d.items():
            if len(v) >= 2:
                ans.append(v)
                
                
        return ans