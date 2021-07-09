class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque(sorted(deck))
        N = len(deck)
        ans = [None for x in range(N)]
        
        cnt = 0
        while d:
            for i in range(N):
                if not ans[i]:
                    cnt += 1
                    if cnt & 1:
                        ans[i] = d.popleft()
                    cnt %= 2
                    
        return ans
        