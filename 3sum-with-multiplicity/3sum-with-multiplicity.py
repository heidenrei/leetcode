import copy

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        N = len(A)
        MOD = 10**9+7
        ans = 0
        d_list = []
        tmp = defaultdict(int)
        tmp[A[0]] = 1
        d_list.append(tmp)
        for i in range(1, N):
            tmp = copy.deepcopy(d_list[i-1])
            tmp[A[i]] += 1
            d_list.append(tmp)
        
        for i in range(2, N):
            for j in range(1, i):
                tmp = target - A[i] - A[j]
                if tmp in d_list[j-1]:
                    ans += d_list[j-1][tmp]
                    ans %= MOD
        
        
        return ans