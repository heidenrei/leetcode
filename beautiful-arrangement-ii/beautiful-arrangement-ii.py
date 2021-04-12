class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        n = deque([x+1 for x in range(n)])
        A = [n.pop()]
        seen = set()
        last_low = False
        while k > 1:
            A.append(n.popleft())
            last_low = True
            k -= 1
            if k > 1:
                A.append(n.pop())
                k -=1
                last_low = False
        
        if not last_low or k == 0:
            A.extend(list(reversed(n)))
        else:
            A.extend(n)
        
        return A