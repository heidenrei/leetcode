class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(x):
            tmp_weights = weights.copy()
            for _ in range(days):
                curr = x
                go = False
                while curr > 0 and not go:
                    tmp = tmp_weights.pop()
                    if tmp > curr:
                        tmp_weights.append(tmp)
                        go = True
                    else:
                        curr -= tmp
                        if len(tmp_weights) == 0:
                            return True
                        
            return False
        
        l = 0
        h = sum(weights)
        
        while l < h:
            m = (l+h) >> 1
            if is_possible(m):
                h = m
            else:
                l = m + 1
                
        return l
                
                
                