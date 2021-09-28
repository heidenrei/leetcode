class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 1)])
        high = 2 ** ceil((log(target) / log(2)))
        seen = {(0, 1)}
        res = 0
        
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                if pos == target:
                    return res
                
                x, y = (pos + speed, speed * 2), (pos, -1 if speed > 0 else 1)
                # limit lower and upper bounds
                if x not in seen and 0 < x[0] <= high:
                    queue.append(x)
                    seen.add(x)
                if y not in seen and 0 < y[0] <= high:
                    queue.append(y)
                    seen.add(y)
            
            res += 1
