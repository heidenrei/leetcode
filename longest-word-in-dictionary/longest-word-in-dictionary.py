class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return ''
        N = len(words)
        d = defaultdict(set)
        
        words.sort()
        
        for i in range(N):
            for j in range(i):
                if abs(len(words[i]) - len(words[j])) == 1:
                    tmp = [words[j], words[i]]
                    if tmp[0] == tmp[1][:len(tmp[0])]:
                        d[tmp[0]].add(tmp[1])
                        
        starter_nodes = [x for x in words if len(x) == 1]
        if not starter_nodes:
            return ''
        best = 1
        curr = set(starter_nodes)
                
        def go(node):
            nonlocal best
            nonlocal curr
            if len(node) > best:
                best = len(node)
                curr = set([node])
            elif len(node) == best:
                curr.add(node)
            for dest in d[node]:
                go(dest)
                
        for node in starter_nodes:
            go(node)
            
        curr = list(curr)
        curr.sort()
        return curr[0]
