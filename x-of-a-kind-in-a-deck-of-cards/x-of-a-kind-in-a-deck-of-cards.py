class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        
        cnts = list(c.values())
        
        return math.gcd(*cnts) >= 2