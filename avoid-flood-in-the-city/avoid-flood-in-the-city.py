import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        cnt = deque()
        lakes = defaultdict(lambda:-1)
        ans = [0]*N
        for i in range(N):
            if rains[i] == 0:
                cnt.append(i)
            else:
                if lakes[rains[i]-1] >= 0:
                    # need to use latest idx > when the lake was filled
                    if cnt:
                        idx = bisect.bisect(cnt, lakes[rains[i]-1])
                        if idx < len(cnt):
                            tmp_idx = cnt[idx]
                            del cnt[idx]
                            ans[tmp_idx] = rains[i]
                            ans[i] = -1
                            lakes[rains[i]-1] = i
                        else:
                            return []
                    else:
                        return []
                else:
                    lakes[rains[i]-1] = i
                    ans[i] = -1
        for idx in cnt:
            ans[idx] = 1
        
        return ans