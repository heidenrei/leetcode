class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter([x for x in text if x in 'balon'])
                
        ans = inf
        
        for ch in 'ban':
            ans = min(c[ch], ans)
        
        for ch in 'lo':
            ans = min(c[ch]//2, ans)
            
        return ans