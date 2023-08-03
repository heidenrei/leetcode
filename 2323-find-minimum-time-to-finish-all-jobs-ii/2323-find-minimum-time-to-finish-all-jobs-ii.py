from sortedcontainers import SortedList

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        N = len(jobs)
        ans = 1
        for i in range(N):
            ans = max(ans, ceil(jobs[i]/workers[i]))
        return int(ans)