class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [x for x in str(num)]
        d = defaultdict(deque)
        N = len(num)
        for i in range(N):
            d[num[i]].append(i)
        #print(d)
        found_ans = False
        for i in range(N):
            if found_ans:
                break
            for b in range(9, int(num[i]), -1):
                if len(d[str(b)]) > 0:
                    b = str(b)
                    #print(b, d[b])
                    num[i], num[d[b][-1]] = num[d[b][-1]], num[i]
                    found_ans = True
                    break
            d[num[i]].popleft()
            if len(d[num[i]]) == 0:
                del d[num[i]]
                    
        return ''.join(num)