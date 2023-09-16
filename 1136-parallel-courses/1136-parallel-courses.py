class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = defaultdict(int)
        d = defaultdict(list)
        roots = set(x for x in range(n))
        for x, y in relations:
            d[x].append(y)
            indegree[y] += 1
            if y in roots:
                roots.remove(y)
                
        q = [x for x in roots]
        level = 0
        while q:
            tmp = []
            while q:
                curr = q.pop()
                for child in d[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        tmp.append(child)
            level += 1
            q = tmp
        for v in indegree.values():
            if v:
                return -1
        return level