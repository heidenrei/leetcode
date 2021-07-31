class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x: (x[1], -x[0]))
        
        for x, y in people:
            cnt = 0
            already_added = False

            if cnt == y:
                ans = [[x, y]] + ans
                continue
            for idx, [ax, ay] in enumerate(ans):
                if cnt == y:
                    ans = ans[:idx] + [[x, y]] + ans[idx:]
                    already_added = True
                    break
                if ax >= x:
                    cnt += 1
                    
            if cnt == y and not already_added:
                ans += [[x, y]]
                    
        return ans