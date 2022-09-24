class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = defaultdict(list)
        for i in range(len(ppid)):
            d[ppid[i]].append(pid[i])
            
        killed = []
        def go(node):
            killed.append(node)
            for child in d[node]:
                go(child)
                
        go(kill)
        return killed