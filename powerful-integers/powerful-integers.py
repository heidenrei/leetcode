class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        if x > y:
            x, y = y, x
        
        if y == 1:
            maxy = 1
        else:
            maxy = math.ceil(math.log(bound, y))
        if x == 1:
            maxx = 1
        else:
            maxx = math.ceil(math.log(bound, x))
                
        for i in range(maxy):
            for j in range(maxx):
                tmp = x**j + y**i
                if tmp <= bound:
                    ans.add(tmp)
        
        return list(ans)