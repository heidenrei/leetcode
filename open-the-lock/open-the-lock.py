class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        visited = set()
        for d in deadends:
            visited.add(d)
            
        q = ['0'*4]
        level = 0
        
        while q:
            tmp = []
            while q:
                curr = q.pop()
                if curr == target:
                    return level
                else:
                    curr = [int(x) for x in curr]
                    for i in range(4):
                        if curr[i] != 0 and curr[i] != 9:
                            tmp.append(''.join([str(x) for x in curr[:i] + [curr[i]-1] + curr[i+1:]]))
                            tmp.append(''.join([str(x) for x in curr[:i] + [curr[i]+1] + curr[i+1:]]))

                        elif curr[i] == 0:
                            tmp.append(''.join([str(x) for x in curr[:i] + [9] + curr[i+1:]]))
                            tmp.append(''.join([str(x) for x in curr[:i] + [curr[i]+1] + curr[i+1:]]))
                        elif curr[i] == 9:
                            tmp.append(''.join([str(x) for x in curr[:i] + [0] + curr[i+1:]]))
                            tmp.append(''.join([str(x) for x in curr[:i] + [curr[i]-1] + curr[i+1:]]))
                            
            level += 1
            for code in tmp:
                if code not in visited:
                    visited.add(code)
                    q.append(code)
                        
        return -1