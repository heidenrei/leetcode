from sortedcontainers import SortedList

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        n += 1
        N = len(tasks)
        c = Counter(tasks)
        sl = SortedList([k for k in c], key=lambda x: c[x])
        ans = 0
        while sl:
            # print(c)
            # print(sl)
            if n >= len(sl):
                cnt = 0
                to_add = []
                for _ in range(len(sl)):
                    x = sl.pop()
                    cnt += 1
                    c[x] -= 1
                    if c[x] > 0:
                        to_add.append(x)
                if to_add:
                    ans += n
                else:
                    ans += cnt
                for ch in to_add:
                    sl.add(ch)
            else:
                to_add = []
                for _ in range(n):
                    x = sl.pop()
                    c[x] -= 1
                    if c[x] > 0:
                        to_add.append(x)
                for ch in to_add:
                    sl.add(ch)
                ans += n
                
        return ans