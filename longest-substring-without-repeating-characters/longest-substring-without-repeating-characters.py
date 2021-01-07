class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
​
        if not s:
            return 0
​
        best = 1
        q = deque([s[0]])
        curr = set([s[0]])
        
        for i in range(1, N):
            while s[i] in curr:
                curr.remove(q.popleft())
            q.append(s[i])
            curr.add(s[i])
            best = max(best, len(q))
            
        return best
