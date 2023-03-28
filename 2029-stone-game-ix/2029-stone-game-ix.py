class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones = [x%3 for x in stones]
        c = Counter(stones)
        x, y, z = min(c[1], c[2]), max(c[1], c[2]), c[0]&1
        print(x, y, z)
        # 1 1 2 1 2 1 2
        # A B A B A B A... even num 0s and more 2s.. A wins
        
        # 2 2 1 2 1 2 1.. even num 0s and more 1s.. A wins
        
        # 2 0 2
        
        
        # start on 1
        tx = x-1
        if x and y > tx and not z:
            return True
        ty = y-1
        if y and  x > ty and not z:
            return True
        if x and z and y < tx-1:
            return True
        if y and z and x < ty-1:
            #print('11')
            return True
        return False