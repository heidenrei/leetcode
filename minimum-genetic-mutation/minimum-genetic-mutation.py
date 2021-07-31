class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        d = defaultdict(list)
        bank += [start]
        N = len(bank)

        seen = set()
        seen.add(N-1)
        
        for i in range(N):
            for j in range(i):
                one = [x for x in bank[i]]
                two = [x for x in bank[j]]
                for k in range(8):
                    if one[:k] + one[k+1:] == two[:k] + two[k+1:]:
                        d[i].append(j)
                        d[j].append(i)
                        break
                
        q = [N-1]
        level = 0
        while q:
            tmp = []
            while q:
                curr = q.pop()
                if bank[curr] == end:
                    return level
                for dest in d[curr]:
                    if dest not in seen:
                        seen.add(dest)
                        tmp.append(dest)
            level += 1      
            q = tmp
            
        return -1