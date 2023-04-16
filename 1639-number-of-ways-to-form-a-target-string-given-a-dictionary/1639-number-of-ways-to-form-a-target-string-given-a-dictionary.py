class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # n, mod = len(target), 10**9 + 7
        # res = [1] + [0] * n
        # for i in range(len(words[0])):
        #     count = Counter(w[i] for w in words)
        #     for j in range(n - 1, -1, -1):
        #         res[j + 1] += res[j] * count[target[j]] % mod
        # return res[n] % mod
    
        N = len(target)
        MOD = 10**9+7
        ans = [1] + [0]*N
        for i in range(len(words[0])):
            cnt = Counter(w[i] for w in words)
            for j in range(N-1, -1, -1):
                ans[j+1] += ans[j] * cnt[target[j]]
                ans[j+1] %= MOD
        return ans[N]