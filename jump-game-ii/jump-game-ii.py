class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        seen = set()
        if N == 1:
            return 0
        q = [0]
        cnt = 0
        
        while q:
            tmp = set()
            while q:
                i = q.pop()
                if i == N - 1:
                    return cnt
                
                if i + nums[i] >= N - 1:
                    return cnt + 1
                
                for di in range(1, nums[i]+1):
                    ni = i + di
                    if ni not in seen:
                        seen.add(ni)
                        tmp.add(ni)
            q.extend(list(tmp))
            cnt += 1