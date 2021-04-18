import bisect

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[x[0], x[1], idx] for idx, x in enumerate(tasks)]
        tasks.sort()
        tasks = deque(tasks)
        h = deque()
        t = 0
        ans = []
        #bs for time <= curr to find search space
        # every new task that is covered gets added to mono inc q where compute time is increasing, and if it's == then sort by idx
        
        while tasks or h:
            #pop from tasks
            if not h:
                x, y, idx = tasks.popleft()
                ans.append(idx)
                t = max(t, x) + y
                n_idx = bisect.bisect_right(tasks, [t, math.inf, math.inf])
                for _ in range(n_idx):
                    _,y,idx = tasks.popleft()
                    bisect.insort(h, [y, idx])
            else:
                y, idx = h.popleft()
                t += y
                ans.append(idx)
                n_idx = bisect.bisect_right(tasks, [t, math.inf, math.inf])
                for _ in range(n_idx):
                    _,y,idx = tasks.popleft()
                    bisect.insort(h, [y, idx])
                    
        return ans