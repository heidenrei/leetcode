class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def md(x,y):
            return abs(x-target[0]) + abs(y-target[1])

        return all(md(*x) > abs(target[0]) + abs(target[1]) for x in ghosts)