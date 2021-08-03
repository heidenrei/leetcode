class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        ans = [[]]
        for x in nums:
            if tuple([x]) not in seen:
                tmp = [[x]]
                seen.add(tuple([x]))
            else:
                tmp = []
            for y in ans:
                tmp_l = sorted([x] + y)
                
                if tuple(tmp_l) not in seen:
                    seen.add(tuple(tmp_l))
                
                    tmp.append([x] + y)
                
            ans.extend(tmp)
            
        return ans