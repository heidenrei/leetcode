class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        N = len(tasks)
        tasks.sort()
        print(tasks)
        @cache
        def go(i, rem, prev):
            if i == N:
                return 0 if rem <= 1 else inf
            ans = inf
            pick = inf
            if tasks[i] == prev and rem:
                pick = go(i+1, rem-1, prev)
            pss = inf
            if rem <= 1:
                pss = go(i+1, 2, tasks[i]) + 1
            return min(pick, pss)
        
        return go(1, 2, tasks[0]) + 1 if go(1, 2, tasks[0]) < inf else -1
                