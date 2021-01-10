class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        
        for i in range(len(encoded)):
​
​
            ans.append(first)
            first ^= encoded[i]
            
        ans.append(first)
        return ans
