class Solution:
    def countVowels(self, word: str) -> int:
        def bc(x):
            return (x*(x+1))//2
        N = len(word)
        ans = 0
        vc = 0
        v = 'aeiou'
        for idx, x in enumerate(word):
            if x in v:
                ans += (idx+1) * (N-idx)
                
        return ans